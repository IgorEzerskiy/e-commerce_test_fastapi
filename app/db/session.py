from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from app.core.config import config
from sqlalchemy.orm import sessionmaker
from typing import Annotated
from fastapi import Depends

engine = create_engine(config.db_settings.url_object)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]
