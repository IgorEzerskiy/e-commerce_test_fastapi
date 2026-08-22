from pydantic import BaseModel
from datetime import datetime

class RoleBase(BaseModel):
    title: str
    is_staff: bool
    is_superuser: bool

class RoleCreate(RoleBase):
    pass

class RoleUpdate(RoleBase):
    pass

class RoleRead(RoleBase):
    id: int
    created_at: datetime
    updated_at: datetime
