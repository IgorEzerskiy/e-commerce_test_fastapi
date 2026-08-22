from fastapi import APIRouter, status, Path, Query
from app.core.logger import get_logger
from app.schemas.category import CategoryRead
from typing import Sequence
from app.api.deps import category_service

logger = get_logger(__name__)

router = APIRouter()

@router.get("/", response_model=Sequence[CategoryRead], status_code=status.HTTP_200_OK)
def read_categories_query(
        service: category_service,
        skip: int = Query(0, ge=0),
        limit: int | None = Query(None, ge=1, le=20)
):
    return service.list(skip=skip, limit=limit)

@router.get("/{id}", response_model=CategoryRead, status_code=status.HTTP_200_OK)
def read_category(
        service: category_service,
        id: int = Path(gt=0)
):
    return service.read(id)

@router.get("/{slug}/", response_model=CategoryRead, status_code=status.HTTP_200_OK)
def read_categories(
        service: category_service,
        slug: str = Path(min_length=1)
):
    return service.read_by_slug(slug=slug)
