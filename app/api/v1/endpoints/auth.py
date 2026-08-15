from fastapi import APIRouter, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.core.logger import get_logger
from app.api.deps import auth_service
from app.schemas.user import UserCreate, UserCreateResponse
from app.schemas.token import Token
from typing import Annotated


logger = get_logger(__name__)

router = APIRouter()

@router.post("/sign_in", response_model=UserCreateResponse, status_code=status.HTTP_201_CREATED)
async def sign_in(service: auth_service, data: UserCreate):
    return service.create_user(data=data)


@router.post("/token", response_model=Token, status_code=status.HTTP_200_OK)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], service: auth_service):
    token = service.get_access_token(form_data.username, form_data.password)

    return {
        "access_token": token,
        "token_type": "bearer"
    }
