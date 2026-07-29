from app.db.base import Base
from sqlalchemy import Column, Integer, DateTime, ForeignKey, UUID, DECIMAL, Text, UniqueConstraint
from sqlalchemy.orm import relationship
from app.utils.time import now_local


class Order(Base):
    __tablename__ = 'order'

    id = Column(
        Integer,
        primary_key=True
    )
    order_number = Column(
        UUID,
        unique=True
    )
    status_id = Column(
        Integer,
        ForeignKey('order_status.id'),
        nullable=False
    )
    client_id = Column(
        Integer,
        ForeignKey('user.id'),
        nullable=False
    )
    manager_id = Column(
        Integer,
        ForeignKey('user.id')
    )
    shipping_id = Column(
        Integer,
        ForeignKey('shipping.id'),
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
    total_price = Column(
        DECIMAL,
        nullable=False
    )
    comment = Column(Text)

    product_links = relationship(
        'OrderProduct',
        back_populates='order'
    )
    status = relationship('OrderStatus')
    client = relationship(
        'User',
        foreign_keys='Order.client_id',
        back_populates='order_as_client'
    )
    manager = relationship(
        'User',
        foreign_keys='Order.manager_id',
        back_populates='order_as_manager'
    )
    shipping = relationship('Shipping')

class OrderProduct(Base):
    __tablename__ = 'order_product'
    __table_args__ = (UniqueConstraint('order_id', 'product_id', name='uq_order_product'),)

    id = Column(
        Integer,
        primary_key=True
    )
    product_id = Column(
        Integer,
        ForeignKey('product.id'),
        nullable=False
    )
    order_id = Column(
        Integer,
        ForeignKey('order.id'),
        nullable=False
    )

    order = relationship(
        'Order',
        back_populates='product_links'
    )
    product = relationship(
        'Product',
        back_populates='order_links'
    )
    price = Column(
        DECIMAL,
        nullable=False
    )
    amount = Column(
        Integer,
        nullable=False
    )
