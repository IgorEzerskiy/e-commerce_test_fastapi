from fastapi import APIRouter
from app.api.v1.endpoints.admin import category

router_v1 = APIRouter()

router_v1.include_router(category.router, prefix="/category", tags=["category"])
