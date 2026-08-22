from fastapi import APIRouter
from app.api.v1.endpoints.admin import category, role

router_admin = APIRouter()

router_admin.include_router(category.router, prefix="/category", tags=["category"])
router_admin.include_router(role.router, prefix="/role", tags=["role"])
