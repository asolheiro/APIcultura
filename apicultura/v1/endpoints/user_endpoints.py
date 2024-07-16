from http import HTTPStatus
from typing import Annotated

from fastapi import APIRouter, Depends

from apicultura.core.models.user_model import User
from apicultura.core.security.user import get_current_user
from apicultura.core.schemas.user_schema import UserIn, UserOut, UserUpdate, UsersList
from apicultura.v1.services.user_services import UserServices

router = APIRouter(prefix="/users", tags=["users"])


CurrentUser = Annotated[User, Depends(get_current_user)]
Services = Annotated[UserServices, Depends(UserServices)]


@router.post("/", status_code=HTTPStatus.CREATED, response_model=UserOut)
def create_user(user: UserIn, service: Services):
    return service.create_user(user_input=user)


@router.get("/{user_id}", status_code=HTTPStatus.OK, response_model=UserOut)
def get_user(user_id: int, service: Services):
    return service.get_user_by_id(user_id=user_id)


@router.get("/view/", status_code=HTTPStatus.OK, response_model=UsersList)
def get_users_listed(service: Services):
    return {'users': service.list_users(limit=10, skip=0)}


@router.put("/{user_id}", status_code=HTTPStatus.OK, response_model=UserOut)
def update_user(
    user_id: int,
    user_update: UserUpdate,
    service: Services,
    current_user: CurrentUser
):
    return service.update_user(
        user_id=user_id, 
        user_update=user_update, 
        current_user=current_user
        )


@router.delete("/{user_id}", status_code=HTTPStatus.NO_CONTENT)
def delete_user(
    user_id: int,
    service: Services,
    current_user: CurrentUser,
):
    return service.delete_user(user_id=user_id, current_user=current_user)
