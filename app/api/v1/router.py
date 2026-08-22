from fastapi import APIRouter
from app.api.v1.endpoints import (healthchek, auth, user, category)
from app.api.v1.endpoints.admin import router as admin_router

router_v1 = APIRouter()

router_v1.include_router(healthchek.router, prefix="/healthcheck", tags=["healthcheck"])
router_v1.include_router(auth.router, prefix="/auth", tags=["auth"])
router_v1.include_router(user.router, prefix="/user", tags=["user"])
router_v1.include_router(category.router, prefix="/category", tags=["category"])
router_v1.include_router(admin_router.router_admin, prefix="/admin", tags=["admin"])
