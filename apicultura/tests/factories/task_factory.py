import factory

import factory.fuzzy
from apicultura.tests.factories.base import BaseFactory
from apicultura.core.models.task_models import Task, TaskStatus
from apicultura.tests.conftest import session


class TaskFactory(BaseFactory):
    title = f"Task test numer {factory.sequence(lambda n: n + 1)}"
    description = factory.Sequence(lambda n: f"description_test_{n}")
    state = factory.fuzzy.FuzzyChoice(TaskStatus)

    class Meta:
        model = Task
        sqlalchemy_session_persistence = "commit"
        sqlalchemy_session = session
