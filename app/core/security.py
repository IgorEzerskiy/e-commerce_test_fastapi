from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timezone, timedelta
from zoneinfo import ZoneInfo
from app.core.config import config
from typing import Union
from app.core.logger import get_logger

logger = get_logger(__name__)

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return bcrypt_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt_context.verify(plain_password, hashed_password)

def jwt_encode(data: dict) -> str:
    encode = data.copy()
    encode.update(
        {'exp': datetime.now(timezone.utc).\
                astimezone(tz=ZoneInfo(config.system_settings.time_zone))\
                + timedelta(minutes=config.system_settings.token_expiration_minutes)
        }
    )

    return jwt.encode(encode, config.system_settings.secret_key, algorithm=config.system_settings.algorithm)

def jwt_decode(token: str) -> Union[dict, None]:
    try:
        payload = jwt.decode(token, config.system_settings.secret_key, algorithms=[config.system_settings.algorithm])
        return payload
    except JWTError as e:
        logger.error(f"jwt error: {e}")
        raise JWTError(e)

def create_access_token(user_id: int) -> str:
    encode = {
        'sub': str(user_id),
    }

    return jwt_encode(data=encode)
