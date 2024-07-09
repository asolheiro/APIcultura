import factory
import factory.faker as faker

from apicultura.core.models.user_model import User
from apicultura.tests.factories.base import BaseFactory

# from apicultura.core.security.password_hash import get_password_hash


def get_user_factory(session):
    class UserFactory(BaseFactory):
        id = factory.sequence(lambda n: n + 1)
        username = faker.Faker("name")
        password = faker.Faker("pystr")
        email = faker.Faker("email")

        class Meta:
            model = User
            sqlalchemy_session_persistence = "commit"
            sqlalchemy_session = session

    return UserFactory


def generate_user(session):
    return get_user_factory(session=session)