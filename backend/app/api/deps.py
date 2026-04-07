from __future__ import annotations

from collections.abc import Generator
from typing import Annotated

from fastapi import Depends, Header, HTTPException
from sqlalchemy.orm import Session

from app.core.config import Settings, get_settings
from app.core.security import verify_google_id_token
from app.db import SessionLocal
from app.repositories.user_repository import UserRepository
from app.services.auth_service import AuthService
from app.services.test_service import TestService


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_user_repository(db: Annotated[Session, Depends(get_db)]) -> UserRepository:
    return UserRepository(db)


def get_auth_service(
    settings: Annotated[Settings, Depends(get_settings)],
    users: Annotated[UserRepository, Depends(get_user_repository)],
) -> AuthService:
    return AuthService(settings, users)


def get_test_service() -> TestService:
    return TestService()


def get_bearer_token(
    authorization: Annotated[str | None, Header(alias="Authorization")] = None,
) -> str:
    if authorization is None or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing bearer token")
    return authorization.removeprefix("Bearer ").strip()


def get_verified_user_email(
    token: Annotated[str, Depends(get_bearer_token)],
    settings: Annotated[Settings, Depends(get_settings)],
) -> str:
    claims = verify_google_id_token(token, settings.google_client_id)
    return claims["email"]

