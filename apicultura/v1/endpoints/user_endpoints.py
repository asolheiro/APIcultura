from http import HTTPStatus

from fastapi import APIRouter, Depends

from apicultura.core.schemas.user_schema import UserIn, UserOut, UserUpdate, UsersList
from apicultura.v1.services.user_services import UserServices

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", status_code=HTTPStatus.CREATED, response_model=UserOut)
def create_user(user: UserIn, service: UserServices = Depends(UserServices)):
    return service.create_user(user_input=user)


@router.get("/{user_id}", status_code=HTTPStatus.OK, response_model=UserOut)
def get_user(user_id: int, service: UserServices = Depends(UserServices)):
    return service.get_user_by_id(user_id=user_id)


@router.get("/view/", status_code=HTTPStatus.OK, response_model=UsersList)
def get_users_listed(service: UserServices = Depends(UserServices)):
    return {'users': service.list_users(limit=10, skip=0)}


@router.put("/{user_id}", status_code=HTTPStatus.OK, response_model=UserOut)
def update_user(
    user_id: int,
    user_update: UserUpdate,
    service: UserServices = Depends(UserServices),
):
    return service.update_user(user_id=user_id, user_update=user_update)


@router.delete("/{user_id}", status_code=HTTPStatus.NO_CONTENT)
def delete_user(user_id: int, service: UserServices = Depends(UserServices)):
    return service.delete_user(user_id=user_id)
