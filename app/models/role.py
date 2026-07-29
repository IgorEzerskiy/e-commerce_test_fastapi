from app.db.base import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from app.utils.time import now_local


class Role(Base):
    __tablename__ = 'role'

    id = Column(
        Integer,
        primary_key=True
    )
    title = Column(
        String(64),
        nullable=False
    )
    is_staff = Column(
        Boolean,
        nullable=False,
        default=False
    )
    is_superuser = Column(
        Boolean,
        nullable=False,
        default=False
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
