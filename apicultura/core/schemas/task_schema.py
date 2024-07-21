from pydantic import BaseModel

from apicultura.core.models.task_models import TaskStatus


class TaskIn(BaseModel):
    title: str
    description: str
    state: TaskStatus


class TaskUpdate(BaseModel):
    title: str
    description: str
    state: TaskStatus


class TaskOut(BaseModel):
    id: int


class TasksList(BaseModel):
    tasks: list[TaskOut]
