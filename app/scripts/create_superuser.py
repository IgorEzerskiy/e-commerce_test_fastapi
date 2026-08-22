import getpass

from app.db.session import SessionLocal
from app.models.user import User
from app.models.role import Role
from app.core.security import hash_password
from app.core.logger import get_logger, setup_logging

setup_logging()
logger = get_logger(__name__)

def create_superuser() -> None:
    db = SessionLocal()
    try:
        admin_role = db.query(Role).filter_by(title="admin", is_superuser=True).first()
        if not admin_role:
            logger.error("No 'admin' superuser role found. Run seed_roles first.")
            return

        email = input("Email: ").strip()

        existing = db.query(User).filter_by(email=email).first()
        if existing:
            logger.error("User with email %s already exists.", email)
            return

        first_name = input("First name: ").strip()
        last_name = input("Last name: ").strip()
        phone_number = input("Phone number: ").strip()

        password = getpass.getpass("Password: ")
        password_confirm = getpass.getpass("Confirm password: ")
        if password != password_confirm:
            logger.error("Passwords do not match.")
            return

        user = User(
            email=email,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            hashed_password=hash_password(password),
            role_id=admin_role.id,
            is_active=True,
        )
        db.add(user)
        db.commit()
        logger.info(f"Superuser created: {email}")

    finally:
        db.close()


if __name__ == "__main__":
    create_superuser()
