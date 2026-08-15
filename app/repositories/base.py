from typing import Generic, TypeVar, Type, Optional, Sequence
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.db.base import Base

ModelType = TypeVar("ModelType", bound=Base)

class BaseRepository(Generic[ModelType]):
    def __init__(self, model: Type[ModelType], db: Session):
        self.model = model
        self.db = db

    def get(self, id: int) -> Optional[ModelType]:
        return self.db.get(self.model, id)

    def list(self, skip: int = 0, limit: int = 20) -> Sequence[ModelType]:
        result = self.db.execute(
            select(self.model).offset(skip).limit(limit)
        )
        return result.scalars().all()

    def create(self, obj: ModelType) -> ModelType:
        self.db.add(obj)
        self.db.flush()      # populate PK, no commit here
        self.db.refresh(obj)
        return obj

    def delete(self, obj: ModelType) -> None:
        self.db.delete(obj)
        self.db.flush()
