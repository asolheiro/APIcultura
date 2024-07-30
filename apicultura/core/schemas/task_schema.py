from pydantic import BaseModel, ConfigDict

from apicultura.core.models.task_models import TaskStatus


class TaskIn(BaseModel):
    title: str
    description: str
    state: TaskStatus = TaskStatus.draft


class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    state: TaskStatus | None = None


class TaskOut(BaseModel):
    id: int


class TasksList(BaseModel):
    Tasks: list[TaskOut]

    model_config = ConfigDict(from_attributes=True)
