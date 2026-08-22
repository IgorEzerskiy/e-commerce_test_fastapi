from app.repositories.base import BaseRepository
from app.models.category import Category


class CategoryRepository(BaseRepository[Category]):
    def __init__(self, db):
        super().__init__(Category, db)

    def get_by_slug(self, slug):
        return self.db.query(Category).filter(Category.slug == slug).first()

    def get_all(self):
        return self.db.query(Category).all()

