from app.db.base import Base
from sqlalchemy import Column, Integer, String


class OrderStatus(Base):
    __tablename__ = 'order_status'
    id = Column(
        Integer,
        primary_key=True
    )
    title = Column(
        String(255),
        nullable=False
    )
