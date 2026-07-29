from app.db.base import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class PostOffice(Base):
    __tablename__ = 'postoffice'

    id = Column(
        Integer,
        primary_key=True
    )
    name = Column(
        String(255),
        nullable=False
    )
    address = Column(
        String(255),
        nullable=False
    )
    number = Column(
        String(255),
        nullable=False
    )
    type_id = Column(
        Integer,
        ForeignKey('postoffice_type.id'),
        nullable=False
    )


class PostOfficeType(Base):
    __tablename__ = 'postoffice_type'

    id = Column(
        Integer,
        primary_key=True
    )
    name = Column(
        String(255),
        nullable=False
    )
