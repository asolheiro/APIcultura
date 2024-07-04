import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.pool import StaticPool

from apicultura.core.dependencies import get_db
from apicultura.core.models.base import Base

# from apicultura.core.security.user import UserSecurity
from apicultura.core.settings import Settings
from apicultura.main import app

# from apicultura.tests.factories.user import get_user_factory

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


# @pytest.fixture(autouse=True, scope="function")
# def token(client):
#     UserFactory = get_user_factory(session)
#     _password = "12345"
#     user = UserFactory(
#         username="admin",
#         password=UserSecurity().get_password_hash(
#             _password,
#         ),
#     )

#     return get_token_from_user(user=user, password=_password, client=client)


# def get_token_from_user(user, password, client):
#     data = {"email": user.email, "password": password}
#     response = client.post(
#         "/v1/auth/", json=data, headers={"content-type": "application/json"}
#     )
#     data = response.json()
#     _token = data["token"]["access_token"]
#     return _token
