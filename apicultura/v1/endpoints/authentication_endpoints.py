from http import HTTPStatus
from typing import Annotated

from fastapi import Depends
from fastapi.routing import APIRouter
from fastapi.security import OAuth2PasswordRequestForm

from apicultura.core.schemas.token_schema import TokenOut
from apicultura.v1.services.token_service import TokenServices


router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

OAuth2Form = Annotated[OAuth2PasswordRequestForm, Depends(OAuth2PasswordRequestForm)]
Services = Annotated[TokenServices, Depends(TokenServices)]

@router.post('/', status_code=HTTPStatus.OK, response_model=TokenOut)
def login_for_access_token(
        form_data: OAuth2Form,
        service: Services,
):
    return service.get_user_token(form_data=form_data)