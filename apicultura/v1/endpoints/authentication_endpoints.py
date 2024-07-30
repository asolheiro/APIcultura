from http import HTTPStatus
from typing import Annotated

from fastapi import Depends
from fastapi.routing import APIRouter
from fastapi.security import OAuth2PasswordRequestForm

from apicultura.core.schemas.token_schema import TokenOut
from apicultura.core.models.user_model import User
from apicultura.v1.services.token_service import TokenServices
from apicultura.core.security.user import get_current_user
from apicultura.core.security.token import crete_access_token


router = APIRouter(prefix="/auth", tags=["auth"])

OAuth2Form = Annotated[
    OAuth2PasswordRequestForm, Depends(OAuth2PasswordRequestForm)
]
Services = Annotated[TokenServices, Depends(TokenServices)]


@router.post("/", status_code=HTTPStatus.OK, response_model=TokenOut)
def login_for_access_token(
    form_data: OAuth2Form,
    service: Services,
):
    return service.get_user_token(form_data=form_data)


@router.post("/refresh", response_model=TokenOut)
def refresh_access_token(
    user: User = Depends(get_current_user),
):
    new_access_token = crete_access_token(data={"sub": user.email})

    return {
        "access_token": new_access_token,
        "token_type": "bearer",
    }
