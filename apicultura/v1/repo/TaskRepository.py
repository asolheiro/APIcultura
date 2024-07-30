from fastapi import Depends
from sqlalchemy import select
from apicultura.core.database import Session
from apicultura.core.models.task_models import Task
from apicultura.core.database import get_session
from apicultura.core.exceptions import NotFoundException


class TaskRepository:
    db: Session
    _model = Task

    def __init__(self, db: Session = Depends(get_session)) -> None:
        self.db = db

    @property
    def base_query(self):
        return (
            self.db.query(self._model)
            .filter(self._model.deleted_at.is_(None))
            .order_by(self._model.created_at.asc())
        )

    def get_task_by_id(self, pk: int) -> Task:
        return self.base_query.filter(self._model.id == pk).first()

    def list_user_tasks(
            self, 
            user_id: int,
            title: str, 
            description: str,
            state: str,
            offset: int,
            limit: int,
        ) -> list[Task]:

        query = select(Task).where(Task.user_id == user_id)

        if title:
            query = query.filter(Task.title.contains(title))
        if description:
            query = query.filter(Task.description.contains(description))
        if state:
            query = query.filter(Task.state.contains(state))

        tasks = self.db.scalars(query.offset(offset).limit(limit)).all()
        return {'Tasks': tasks}

    def create(self, task: Task) -> Task:
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return task

    def update(self, **updated_values) -> Task:
        db_task = self.db.scalar(
            select(Task).where(Task.id == updated_values["task_id"])
        )
        if not db_task:
            raise NotFoundException("Task not found")
        for key, value in updated_values.items():
            setattr(db_task, key, value)
        self.db.add(db_task)
        self.db.commit()
        self.db.refresh(db_task)
        return db_task

    def delete(self, task_id: int):
        task = self.db.scalar(select(Task).where(Task.id == task_id))
        if not task:
            raise NotFoundException("Task not found")

        self.db.delete(task)
        self.db.commit()
