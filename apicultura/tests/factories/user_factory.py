import factory
import factory.faker as faker

from apicultura.core.models.user_model import User
from apicultura.tests.conftest import session
from apicultura.tests.factories.base import BaseFactory


class UserFactory(BaseFactory):
    id = factory.sequence(lambda n: n + 1)
    username = faker.Faker("name")
    password = faker.Faker("pystr")
    email = faker.Faker("email")

    class Meta:
        model = User
        sqlalchemy_session_persistence = "commit"
        sqlalchemy_session = session
