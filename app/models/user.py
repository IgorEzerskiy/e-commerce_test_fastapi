from app.db.base import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.utils.time import now_local

class User(Base):
    __tablename__ = 'user'
    id = Column(
        Integer,
        primary_key=True
    )
    first_name = Column(
        String(60),
        nullable=False
    )
    last_name = Column(
        String(60),
        nullable=False
    )
    phone_number = Column(
        String(20),
        unique=True,
        nullable=False
    )
    email = Column(
        String(255),
        unique=True,
        nullable=False
    )
    role_id = Column(
        Integer,
        ForeignKey('role.id')
    )
    hashed_password = Column(
        String,
        nullable=False
    )
    is_active = Column(
        Boolean,
        default=True,
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
    role = relationship('Role', back_populates='users')
