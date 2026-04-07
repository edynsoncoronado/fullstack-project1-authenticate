from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.api.login import router as login_router
from app.api.test_print import router as test_print_router
from app.db import get_engine
from app.domain.errors import InvalidGoogleTokenError
from app.models import user as _user_model  # noqa: F401 - register ORM mappers
from app.models.base import Base


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=get_engine())
    yield


app = FastAPI(lifespan=lifespan)


@app.exception_handler(InvalidGoogleTokenError)
async def invalid_google_token_handler(
    request: Request,
    exc: InvalidGoogleTokenError,
):
    return JSONResponse(
        status_code=401,
        content={"detail": "Invalid or unauthorized token"},
    )


app.include_router(login_router, prefix="/api")
app.include_router(test_print_router, prefix="/api")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}

