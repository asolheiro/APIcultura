import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.pool import StaticPool
from testcontainers.postgres import PostgresContainer

from apicultura.core.dependencies import get_db
from apicultura.core.models.base import Base
from apicultura.core.settings import Settings
from apicultura.main import app

from apicultura.tests.factories.user_factory import get_user_factory

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
    print("setup")
    Base.metadata.create_all(bind=engine)
    yield "resource"
    print("teardown")
    Base.metadata.drop_all(bind=engine)


@pytest.fixture()
def client():
    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as _client:
        yield _client
    app.dependency_overrides.clear()


UserFactory = get_user_factory(session=session)


# Também pode ser usaddo para criar containers de testes
#
# @pytest.fixture(scope='session')
# def engine():
#     with PostgresContainer('postgres:16', driver='psycopg') as postgres:
#         _engine = create_engine(postgres.get_connection_url())
#         with _engine.begin():
#           yield _engine

# @pytest.fixture
# def client(engine):
#     with PostgresContainer('postgres:16', driver='psycopg') as postgres:
#         engine = create_engine(postgres.get_connection_url())
#         table_registry.metadata.create_all(engine)

#         with Session(engine) as session:
#             yield session
#             session.rollback()
#         table_registry.metadata.drop_all(engine)

@pytest.fixture()
def user(client):
    data = {
        "username": "karl",
        "email": "karl@pep.com",
        "password": "ItsASecret",
    }
    response = client.post(url="/v1/users/", json=data)
    data.update({"id": response.json()["id"]})
    return data


@pytest.fixture()
def user_2(client):
    data = {
        "username": "pep",
        "email": "pep@pep.com",
        "password": "ItsASecret",
    }
    response = client.post(url="/v1/users/", json=data)

    data.update({"id": response.json()["id"]})
    return data


@pytest.fixture()
def users():
    return UserFactory.create_batch(5)


@pytest.fixture()
def token(client, user):
    response = client.post(
        "/v1/auth/",
        data={"username": user["email"], "password": user["password"]},
    )

    return response.json()["access_token"]
