from app.db.base import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text, CheckConstraint, Numeric
from sqlalchemy.orm import relationship
from app.utils.time import now_local


class Product(Base):
    __tablename__ = 'product'
    __table_args__ = (
        CheckConstraint('discount >= 0 AND discount <= 100', name='ck_product_discount'),
    )

    id = Column(
        Integer,
        primary_key=True
    )
    title = Column(
        String(255),
        nullable=False
    )
    slug = Column(
        String(255),
        nullable=False,
        unique=True
    )
    description = Column(Text)
    price = Column(
        Numeric(12, 2),
        nullable=False
    )
    discount = Column(Integer)
    meta_title = Column(String(255))
    meta_description = Column(Text)
    quantity = Column(
        Integer,
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
    is_active = Column(
        Boolean,
        default=True
    )

    specifications = relationship(
        'Specification',
        secondary='specification_product',
        back_populates='products'
    )
    categories = relationship(
        'Category',
        secondary='category_product',
        back_populates='products'
    )
    attachments = relationship(
        'Attachment',
        back_populates='product'
    )
    order_links = relationship(
        'OrderProduct',
        back_populates='product'
    )
