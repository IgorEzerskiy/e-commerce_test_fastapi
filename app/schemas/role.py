from pydantic import BaseModel

class RoleBase(BaseModel):
    id: int
    title: str
    is_staff: bool
    is_superuser: bool
