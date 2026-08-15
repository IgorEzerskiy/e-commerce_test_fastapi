from fastapi import Request
from fastapi.responses import JSONResponse

class AppError(Exception):
    status_code = 400
    def __init__(self, message: str):
        self.message = message

class BadRequestError(AppError):
    status_code = 400

class NotFoundError(AppError):
    status_code = 404

class ConflictError(AppError):
    status_code = 409

class UnauthorizedError(AppError):
    status_code = 401

async def app_error_handler(request: Request, exc: AppError):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message},
    )
