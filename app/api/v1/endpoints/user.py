from fastapi import APIRouter, status
from app.core.logger import get_logger
from app.schemas.user import UserReadResponse
from app.api.deps import current_user_deps


logger = get_logger(__name__)

router = APIRouter()

@router.get("/me", response_model=UserReadResponse, status_code=status.HTTP_200_OK)
def read_current_user(user: current_user_deps):
    return user
