from app.db.base import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Shipping(Base):
    __tablename__ = 'shipping'

    id = Column(
        Integer,
        primary_key=True
    )
    address = Column(String(255))
    payment_type_id = Column(
        Integer,
        ForeignKey('payment_type.id'),
        nullable=False
    )
    postoffice_id = Column(
        Integer,
        ForeignKey('postoffice.id'),
        nullable=False
    )
