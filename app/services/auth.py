from app.models import User
from app.repositories.user import UserRepository
from app.core.exceptions import NotFoundError, BadRequestError, UnauthorizedError
from app.core.security import verify_password, hash_password, create_access_token
from app.schemas.user import UserCreate


class AuthService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def __authenticate(self, email: str, password: str) -> User:
        user = self.repo.get_by_email(email=email)

        if not user:
            raise NotFoundError(message="User not found.")

        if not verify_password(password, user.hashed_password):
            raise UnauthorizedError(message="Failed to authenticate.")

        return user

    def create_user(self, data: UserCreate) -> User:
        hashed_password = hash_password(password=data.password)

        user = self.repo.create(User(
            email=data.email,
            phone_number=data.phone_number,
            hashed_password=hashed_password,
            first_name=data.first_name,
            last_name=data.last_name,
        ))

        if not user:
            raise BadRequestError(message="Can't create user.")

        return user

    def get_access_token(self, email: str, password: str) -> str:
        user = self.__authenticate(email=email, password=password)

        token = create_access_token(user.id)

        return token
