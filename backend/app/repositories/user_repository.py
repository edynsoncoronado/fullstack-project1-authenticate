from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.user import User


class UserRepository:
    def __init__(self, session: Session) -> None:
        self._session = session

    def get_by_email(self, email: str) -> User | None:
        return self._session.scalar(select(User).where(User.email == email))

    def create(
        self,
        *,
        email: str,
        name: str | None,
        picture: str | None,
    ) -> User:
        user = User(email=email, name=name, picture=picture)
        self._session.add(user)
        self._session.commit()
        self._session.refresh(user)
        return user

