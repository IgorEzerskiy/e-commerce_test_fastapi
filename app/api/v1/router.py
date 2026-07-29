from fastapi import APIRouter
from app.api.v1.endpoints import (healthchek)

router_v1 = APIRouter()

router_v1.include_router(healthchek.router, prefix="/healthcheck", tags=["healthcheck"])
