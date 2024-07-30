from http import HTTPStatus
from fastapi import APIRouter, Depends, Query
from typing import Annotated


from apicultura.core.models.user_model import User
from apicultura.core.schemas.task_schema import (
    TaskIn,
    TaskOut,
    TaskUpdate,
    TasksList,
)
from apicultura.v1.services.task_services import TaskServices
from apicultura.core.security.user import get_current_user


router = APIRouter(prefix="/task", tags=["task"])

CurrentUser = Annotated[User, Depends(get_current_user)]
Services = Annotated[TaskServices, Depends(TaskServices)]


@router.post("/", status_code=HTTPStatus.CREATED, response_model=TaskOut)
def create_task(
    task_input: TaskIn, service: Services, current_user: CurrentUser
):
    return service.create_task_with_user(
        task_input=task_input, current_user=current_user
    )


@router.get("/{task_id}", status_code=HTTPStatus.OK, response_model=TaskOut)
def get_task(task_id: int, service: Services, current_user: CurrentUser):
    return service.get_user_task_by_id(
        task_id=task_id, current_user=current_user
    )


@router.get("/", status_code=200, response_model=TasksList)
def get_tasks_list(service: Services, 
                   current_user: CurrentUser,
                   title: str = Query(None),
                   description: str = Query(None),
                   state: str = Query(None),
                   offset: str = Query(None),
                   limit: int = Query(None),
                   ):
    return service.list_user_tasks(
        current_user=current_user, 
        title=title, 
        description=description,
        state=state,
        offset=offset,
        limit=limit,
        )


@router.put("/{task_id}", status_code=HTTPStatus.OK, response_model=TaskOut)
def update_task(
    task_id: int,
    task_update: TaskUpdate,
    service: Services,
    current_user: CurrentUser,
):
    return service.update_task(
        task_id=task_id, task_update=task_update, current_user=current_user
    )


@router.delete("/{task_id}", status_code=HTTPStatus.NO_CONTENT)
def delete_task(task_id: int, service: Services, current_user: CurrentUser):
    return service.delete_task(task_id=task_id, current_user=current_user)
