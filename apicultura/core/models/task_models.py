from enum import Enum

from sqlalchemy import ForeignKey, String, Column, Integer
from sqlalchemy.orm import (
    relationship,
)

from apicultura.core.models.base import BModel, ChoiceType


class TaskStatus(str, Enum):
    draft = "draft"
    todo = "todo"
    doing = "doing"
    done = "done"
    trash = "trash"

    def __str__(self):
        return self.value


class Task(BModel):
    __tablename__ = "tasks"

    title = Column(String())
    description = Column(String())
    state = Column(
        ChoiceType(TaskStatus),
        nullable=False,
        default=TaskStatus.todo.value,
    )
    user_id = Column(Integer(), ForeignKey("users.id"))
    user = relationship("User")
