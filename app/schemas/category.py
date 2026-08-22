from pydantic import BaseModel, Field


class CategoryBase(BaseModel):
    title: str = Field(
        str,
        min_length=1,
        max_length=255
    )
    description: str = Field(
        str,
        min_length=1,
        max_length=5000
    )
    meta_title: str = Field(
        str,
        min_length=1,
        max_length=255
    )
    meta_description: str = Field(
        str,
        min_length=1,
        max_length=5000
    )


class CategoryRead(CategoryBase):
    id: int
    slug: str = Field(
        str,
        min_length=1,
        max_length=255
    )


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(CategoryBase):
    pass
