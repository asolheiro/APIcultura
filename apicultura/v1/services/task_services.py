from fastapi import Depends
from apicultura.core.exceptions import CredentialsException, NotFoundException
from apicultura.core.models.task_models import Task
from apicultura.core.models.user_model import User
from apicultura.core.schemas.task_schema import TaskIn, TaskUpdate
from apicultura.v1.repo.TaskRepository import TaskRepository


class TaskServices:
    def __init__(self, repo: TaskRepository = Depends(TaskRepository)) -> None:
        self.repo = repo

    def create_task(self, task_input: TaskIn, current_user: User):
        """Create a new task to an logged user"""

        if not current_user:
            raise CredentialsException("Not enough permissions")

        db_task = Task(
            title=task_input.title,
            description=task_input.description,
            state=task_input.state,
            user_id=current_user.id,
        )

        return self.repo.create(task=db_task)

    def get_user_task_by_id(self, task_id: int, current_user: User):
        """Get an user task by id"""

        db_task = self.repo.get_task_by_id(pk=task_id)
        if not db_task:
            raise NotFoundException("Task not found")

        if current_user.id != db_task.user_id:
            raise CredentialsException("Not enough permissions")
        return db_task

    def list_user_tasks(self, current_user: User):
        """List all user tasks"""

        db_tasks = self.repo.list_user_tasks(user_id=current_user.id)
        if not db_tasks:
            raise NotFoundException("Task not found")

        if current_user.id != db_tasks[0].user_id:
            raise CredentialsException("Not enough permissions")

        return db_tasks

    def update_task(
        self, task_id: int, task_update: TaskUpdate, current_user: User
    ):
        """Update an existins user task"""
        db_task = self.repo.get_task_by_id(pk=task_id)
        if not db_task:
            raise NotFoundException("Task not found")

        if current_user.id != db_task.user_id:
            raise CredentialsException("Not enough permissions")

        updated_values = task_update.model_dump(exclude_unset=True)
        db_task = self.repo.update(task_id=task_id, **updated_values)

        return db_task

    def delete_task(self, task_id: int, current_user: User):
        """Delete an existing user task"""

        db_task = self.repo.get_task_by_id(pk=task_id)
        if not db_task:
            raise NotFoundException("Task not found")

        if current_user.id != db_task.user_id:
            raise CredentialsException("Not enough permissions")

        self.repo.delete(task_id=task_id)
