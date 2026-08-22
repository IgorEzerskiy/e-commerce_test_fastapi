from app.db.session import SessionLocal
from app.models.role import Role
from app.core.logger import get_logger, setup_logging

setup_logging()
logger = get_logger(__name__)

DEFAULT_ROLES = [
    {"title": "admin",  "is_staff": True,  "is_superuser": True},
    {"title": "staff",  "is_staff": True,  "is_superuser": False},
    {"title": "client", "is_staff": False, "is_superuser": False},
]

def seed_roles() -> None:
    db = SessionLocal()
    try:
        for role_data in DEFAULT_ROLES:
            exists = db.query(Role).filter_by(title=role_data["title"]).first()
            if not exists:
                logger.debug(f"Created role: {role_data['title']}")
                db.add(Role(**role_data))
            else:
                logger.warning(f"Role already exists: {role_data['title']}")
        db.commit()
    finally:
        db.close()

if __name__ == "__main__":
    logger.info("Seeding roles")
    seed_roles()
    logger.info("Done")
