from fastapi import APIRouter
from app.api.v1.endpoints.admin import category

router_admin = APIRouter()

router_admin.include_router(category.router, prefix="/category", tags=["category"])
