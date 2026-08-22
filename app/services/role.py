from app.models.role import Role
from app.repositories.role import RoleRepository
from typing import Sequence
from app.core.exceptions import NotFoundError, BadRequestError
from app.schemas.role import RoleCreate, RoleUpdate


class RoleService:
    def __init__(self, repo: RoleRepository):
        self.repo = repo

    def read(self, id: int) -> Role:
        role = self.repo.get(id)
        if role is None:
            raise NotFoundError("Role not found")
        return role

    def find_by_title(self, title: str) -> Role:
        role = self.repo.find_by_title(title)
        if role is None:
            raise NotFoundError("Role not found")
        return role

    def list(self, skip: int = 0, limit: int | None = 20) -> Sequence[Role]:
        roles = self.repo.list(skip=skip, limit=limit)
        return roles

    def create(self, data: RoleCreate) -> Role:
        existing_role = self.repo.find_by_title(data.title)
        if existing_role:
            raise BadRequestError("Role already exists")

        role = self.repo.create(Role(**data.model_dump()))
        return role

    def update(self, id: int, data: RoleUpdate) -> Role:
        role = self.read(id)
        if role is None:
            raise NotFoundError("Role not found")

        for field, value in data.model_dump(exclude_unset=True).items():
            if field == "title" and role.title != data.title:
                existing_role = self.repo.find_by_title(data.title)
                if existing_role is not None:
                    raise BadRequestError("Role with this title already exists.")
                setattr(role, field, value)
            setattr(role, field, value)
        self.repo.db.flush()
        return role

    def delete(self, id: int):
        role = self.read(id)
        if role is None:
            raise NotFoundError("Role not found")
        self.repo.db.delete(role)
