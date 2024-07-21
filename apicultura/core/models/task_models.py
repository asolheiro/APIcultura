from datetime import datetime
from enum import Enum

from sqlalchemy import ForeignKey
from sqlalchemy.orm import (
    relationship,
    mapped_column,
    Mapped,
)

from apicultura.core.models.base import BModel
from apicultura.core.models.user_model import User


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

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    tutle: Mapped[str]
    description: Mapped[str]
    state: Mapped[TaskStatus]

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped[User] = relationship(init=False, back_populates="tasks")
