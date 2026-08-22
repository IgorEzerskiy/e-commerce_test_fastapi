from typing import List, Sequence
from slugify import slugify
from app.models.category import Category
from app.core.exceptions import NotFoundError, BadRequestError
from app.repositories.category import CategoryRepository
from app.schemas.category import CategoryCreate, CategoryUpdate


class CategoryService:
    def __init__(self, repo: CategoryRepository):
        self.repo = repo

    def read(self, id: int) -> Category:
        category = self.repo.get(id)

        if category is None:
            raise NotFoundError("Category not found.")

        return category

    def read_by_slug(self, slug: str) -> Category:
        category = self.repo.get_by_slug(slug)

        if category is None:
            raise NotFoundError("Category not found.")

        return category

    def read_all(self) -> List[Category]:
        categories = self.repo.get_all()

        return categories

    def list(self, skip: int = 0, limit: int | None = 20) -> Sequence[Category]:
        categories = self.repo.list(skip=skip, limit=limit)
        return categories

    def create(self, data: CategoryCreate) -> Category:
        try:
            slug = slugify(data.title)

            existing_category = self.repo.get_by_slug(slug)
            if existing_category is not None:
                raise BadRequestError("Category with this slug already exists.")

            category = self.repo.create(Category(**data.model_dump(), slug=slug))
        except Exception as e:
            raise BadRequestError(f"Failed to create category {data.model_dump()}: {e}")

        return category

    def update(self, id: int, data: CategoryUpdate) -> Category:
        category = self.read(id)
        slug = slugify(data.title)

        for field, value in data.model_dump(exclude_unset=True).items():
            if field == "title" and category.title != data.title:
                existing_category = self.repo.get_by_slug(slug)
                if existing_category is not None:
                    raise BadRequestError("Category with this slug already exists.")
                setattr(category, "slug", slug)
            setattr(category, field, value)
        self.repo.db.flush()
        return category

    def delete(self, id: int) -> None:
        category = self.repo.get(id)

        if category is None:
            raise NotFoundError("Category not found.")
        self.repo.delete(category)
