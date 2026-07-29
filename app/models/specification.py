from app.db.base import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, Text, Table
from sqlalchemy.orm import relationship
from app.utils.time import now_local


specification_product = Table(
    "specification_product",
    Base.metadata,
    Column("specification_id", Integer, ForeignKey("specification.id"), primary_key=True),
    Column("product_id", Integer, ForeignKey("product.id"), primary_key=True),
)


class Specification(Base):
    __tablename__ = 'specification'

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
    value = Column(
        String(255),
        nullable=False
    )
    is_filter = Column(
        Boolean,
        nullable=False,
        default=False
    )
    filter_key = Column(
        String(255),
        nullable=False
    )
    filter_value = Column(
        String(255),
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
        secondary='specification_product',
        back_populates='specifications'
    )
