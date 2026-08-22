from typing import Sequence

from fastapi import APIRouter, status, Query, Path
from app.core.logger import get_logger
from app.schemas.role import RoleCreate, RoleUpdate, RoleRead
from app.api.deps import role_service, superuser_deps

logger = get_logger(__name__)

router = APIRouter()

@router.get("/{id}", response_model=RoleRead, status_code=status.HTTP_200_OK)
def read_role(
        user: superuser_deps,
        service: role_service,
        id: int = Path(gt=0)
):
    """
        Superuser permission required.
    """
    return service.read(id)

@router.get("/{title}/", response_model=RoleRead, status_code=status.HTTP_200_OK)
def find_by_title(
        user: superuser_deps,
        service: role_service,
        title: str = Path(min_length=1)
):
    """
        Superuser permission required.
    """
    return service.find_by_title(title=title)

@router.get("/", response_model=Sequence[RoleRead], status_code=status.HTTP_200_OK)
def read_roles_query(
        user: superuser_deps,
        service: role_service,
        skip: int = Query(0, ge=0),
        limit: int | None = Query(None, ge=1, le=20)
):
    """
        Superuser permission required.
    """
    return service.list(skip=skip, limit=limit)

@router.post("/", response_model=RoleRead, status_code=status.HTTP_201_CREATED)
def create_role(
        user: superuser_deps,
        service: role_service,
        data: RoleCreate
):
    """
        Superuser permission required.
    """
    return service.create(data)

@router.put("/{id}", response_model=RoleRead, status_code=status.HTTP_200_OK)
def update_role(
        user: superuser_deps,
        service: role_service,
        data: RoleUpdate,
        id: int = Path(gt=0)
):
    """
        Superuser permission required.
    """
    return service.update(id, data)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_role(
        user: superuser_deps,
        service: role_service,
        id: int = Path(gt=0)
):
    """
        Superuser permission required.
    """
    return service.delete(id)
