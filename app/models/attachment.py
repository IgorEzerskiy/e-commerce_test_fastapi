from app.db.base import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Attachment(Base):
    __tablename__ = 'attachment'

    id = Column(Integer, primary_key=True)
    image_url = Column(
        String,
        nullable=False
    )
    product_id = Column(
        Integer,
        ForeignKey('product.id'),
        nullable=False
    )
    product = relationship(
        'Product',
        back_populates='attachments'
    )
