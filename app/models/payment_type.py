from app.db.base import Base
from sqlalchemy import Column, Integer, String


class PaymentType(Base):
    __tablename__ = 'payment_type'

    id = Column(
        Integer,
        primary_key=True
    )
    name = Column(
        String(255),
        nullable=False
    )
