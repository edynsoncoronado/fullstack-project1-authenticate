from __future__ import annotations

from google.auth.transport import requests as google_requests
from google.oauth2 import id_token

from app.domain.errors import InvalidGoogleTokenError


def verify_google_id_token(raw_token: str, audience: str) -> dict[str, str | None]:
    """
    Validate a Google OAuth ID token and return stable user claims.

    :raises InvalidGoogleTokenError: If verification fails or required claims are missing.
    """
    try:
        payload = id_token.verify_oauth2_token(
            raw_token,
            google_requests.Request(),
            audience,
        )
    except ValueError as exc:
        raise InvalidGoogleTokenError from exc

    email = payload.get("email")
    if not email or not isinstance(email, str):
        raise InvalidGoogleTokenError()

    if payload.get("email_verified") is False:
        raise InvalidGoogleTokenError()

    name = payload.get("name")
    picture = payload.get("picture")
    return {
        "email": email,
        "name": name if isinstance(name, str) else None,
        "picture": picture if isinstance(picture, str) else None,
    }

