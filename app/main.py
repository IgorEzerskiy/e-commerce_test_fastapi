from fastapi import FastAPI
from app.api.v1.router import router_v1
from contextlib import asynccontextmanager
from app.core.logger import setup_logging


@asynccontextmanager
async def lifespan(app: FastAPI):
    setup_logging()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(router_v1, prefix="/v1")
