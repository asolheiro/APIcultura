import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.pool import StaticPool

from apicultura.core.dependencies import get_db
from apicultura.core.models.base import Base
from apicultura.core.models.user_model import User
from apicultura.core.settings import Settings
from apicultura.main import app

from apicultura.tests.factories.user_factory import get_user_factory
from apicultura.core.security.password_hash import get_password_hash

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

@pytest.fixture()
def user(client) -> User:
    return UserFactory(
        username='karl',
        email='karl@pep.com',
        password=get_password_hash('ItsASecret'),
    )


@pytest.fixture()
def users(client):
    return UserFactory.create_batch(5)


@pytest.fixture()
def token(client, user):
    response = client.post(
        'v1/auth/',
        data = {
            'username': user.email,
            'password': 'ItsASecret'
        }
    )

    return response.json()['access_token']