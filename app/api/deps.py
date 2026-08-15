from fastapi import Depends, HTTPException, status
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer
from app.models.user import User
from jose import JWTError
from app.core.security import jwt_decode
from sqlalchemy.orm import selectinload
from sqlalchemy import select
from app.db.session import db_dependency
from app.repositories.user import UserRepository
from app.services.auth import AuthService


oauth2_bearer = OAuth2PasswordBearer(tokenUrl="/v1/auth/token")

def get_current_user(
        token: Annotated[str, Depends(oauth2_bearer)],
        db: db_dependency) -> User:
    credentials_exc = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt_decode(token)
        user_id = payload.get("sub")

        if user_id is None:
            raise credentials_exc
    except JWTError:
        raise credentials_exc

    user = db.execute(
        select(User)
        .where(User.id == int(user_id))
        .options(selectinload(User.role))
    )

    user = user.scalar_one_or_none()

    if user is None:
        raise credentials_exc

    return user

def get_current_active_user(user: Annotated[User, Depends(get_current_user)]) -> User:
    if not user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")

    return user

def require_staff(user: Annotated[User, Depends(get_current_user)]) -> User:
    if not (user.role.is_staff or user.role.is_superuser):
        raise HTTPException(status_code=403, detail="Staff access required")

    return user

def require_superuser(user: Annotated[User, Depends(get_current_user)]) -> User:
    if not user.role.is_superuser:
        raise HTTPException(status_code=403, detail="Superuser access required")

    return user

current_user_deps = Annotated[User, Depends(get_current_user)]
staff_user_deps = Annotated[User, Depends(require_staff)]
superuser_deps = Annotated[User, Depends(require_superuser)]

def get_user_repo(db: db_dependency) -> UserRepository:
    return UserRepository(db)

def get_auth_service(repo: Annotated[UserRepository, Depends(get_user_repo)]) -> AuthService:
    return AuthService(repo)

auth_service = Annotated[AuthService, Depends(get_auth_service)]
