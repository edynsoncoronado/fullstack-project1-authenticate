from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import get_settings

_engine = create_engine(get_settings().database_url, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=_engine)


def get_engine():
    return _engine

