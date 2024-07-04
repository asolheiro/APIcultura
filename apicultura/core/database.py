from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from apicultura.core.settings import Settings

engine = create_engine(Settings().DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_session():
    with Session(engine) as session:
        yield session
