from fastapi import APIRouter, status, Path
from app.core.logger import get_logger
from app.schemas.category import CategoryCreate, CategoryUpdate, CategoryRead
from app.api.deps import category_service, superuser_deps

logger = get_logger(__name__)

router = APIRouter()

@router.post("/", response_model=CategoryRead, status_code=status.HTTP_201_CREATED)
def create_category(
        user: superuser_deps,
        service: category_service,
        data: CategoryCreate
):
    """
        Superuser permission required.
    """
    return service.create(data)

@router.put("/{id}", response_model=CategoryRead, status_code=status.HTTP_200_OK)
def update_category(
        user: superuser_deps,
        service: category_service,
        data: CategoryUpdate,
        id: int = Path(gt=0)
):
    """
        Superuser permission required.
    """
    return service.update(id, data)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_category(
        user: superuser_deps,
        service: category_service,
        id: int = Path(gt=0)
):
    """
        Superuser permission required.
    """
    service.delete(id)
