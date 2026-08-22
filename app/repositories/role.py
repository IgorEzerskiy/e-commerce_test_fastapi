from app.repositories.base import BaseRepository
from app.models.role import Role


class RoleRepository(BaseRepository[Role]):
    def __init__(self, db):
        super().__init__(Role, db)

    def find_by_title(self, title):
        return self.db.query(Role).filter(Role.title == title).first()
