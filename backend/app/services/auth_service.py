from __future__ import annotations

from app.core.config import Settings
from app.core.security import verify_google_id_token
from app.repositories.user_repository import UserRepository


class AuthService:
    """Handles Google-authenticated login and user persistence."""

    def __init__(self, settings: Settings, users: UserRepository) -> None:
        self._settings = settings
        self._users = users

    def login_with_google_id_token(self, raw_id_token: str) -> None:
        claims = verify_google_id_token(raw_id_token, self._settings.google_client_id)

        existing = self._users.get_by_email(claims["email"])
        if existing is not None:
            return

        self._users.create(
            email=claims["email"],
            name=claims["name"],
            picture=claims["picture"],
        )

