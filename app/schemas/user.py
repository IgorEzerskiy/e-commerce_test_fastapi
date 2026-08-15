from pydantic import BaseModel, ConfigDict
from app.schemas.role import RoleBase


class UserBase(BaseModel):
    phone_number: str
    email: str
    first_name: str
    last_name: str


class UserCreate(UserBase):
    password: str


class UserCreateResponse(UserBase):
    id: int

class UserReadResponse(UserBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    role: RoleBase | None = None
