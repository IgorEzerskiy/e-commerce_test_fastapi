from app.db.base import Base
from sqlalchemy import Column, Integer, String, DateTime, Text, Table, ForeignKey
from sqlalchemy.orm import relationship
from app.utils.time import now_local


category_product = Table(
    "category_product",
    Base.metadata,
    Column("category_id", Integer, ForeignKey("category.id"), primary_key=True),
    Column("product_id", Integer, ForeignKey("product.id"), primary_key=True),
)


class Category(Base):
    __tablename__ = 'category'

    id = Column(
        Integer,
        primary_key=True
    )
    title = Column(
        String(255),
        nullable=False
    )
    description = Column(
        Text,
        nullable=False
    )
    meta_title = Column(
        String(255),
        nullable=False
    )
    meta_description = Column(
        Text,
        nullable=False
    )
    created_at = Column(
        DateTime(timezone=True),
        default=now_local
    )
    updated_at = Column(
        DateTime(timezone=True),
        default=now_local,
        onupdate=now_local
    )

    products = relationship(
        'Product',
        secondary='category_product',
        back_populates='categories'
    )
