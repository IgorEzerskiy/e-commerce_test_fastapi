from fastapi import APIRouter
from app.api.v1.endpoints import (healthchek, auth, user)

router_v1 = APIRouter()

router_v1.include_router(healthchek.router, prefix="/healthcheck", tags=["healthcheck"])
router_v1.include_router(auth.router, prefix="/auth", tags=["auth"])
router_v1.include_router(user.router, prefix="/user", tags=["user"])
