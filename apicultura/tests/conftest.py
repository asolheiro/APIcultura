import pytest
from fastapi.testclient import TestClient
<<<<<<< HEAD

from apicultura.v1.main import app


@pytest.fixture()
def client():
    return TestClient(app)
=======
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, scoped_session, sessionmaker
from sqlalchemy.pool import StaticPool

from apicultura.core.dependencies import get_db
from apicultura.core.models.base import Base
from apicultura.core.settings import Settings
from apicultura.v1.main import app

settings = Settings()


engine = create_engine(
    settings.DATABASE_URL,
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)
session = scoped_session(TestingSessionLocal)


def override_get_db():
    try:
        db = TestingSessionLocal()
        db.begin()
        yield db
    finally:
        db.rollback()
        db.close()


@pytest.fixture(autouse=True)
def resource():
    print('SetUp')
    Base.metadata.create_all(bind=engine)
    yield 'resource'

    print('TearDown')
    Base.metadata.drop_all(bind=engine)


@pytest.fixture()
def session():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        yield session

    Base.metadata.drop_all(engine)


@pytest.fixture()
def client():
    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as _client:
        yield _client

    app.dependency_overrides.clear()
>>>>>>> a694a75 (Primeira migração com alembic. Adicionando a tabela users)
