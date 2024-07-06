from http import HTTPStatus

from fastapi import Depends
from fastapi.routing import APIRouter
from fastapi.security import OAuth2PasswordRequestForm

from apicultura.core.schemas.token_schema import TokenOut
from apicultura.v1.services.token_service import TokenServices


router = APIRouter(
    prefix="/token",
    tags=["token"]
)

@router.post('/', status_code=HTTPStatus.OK, response_model=TokenOut)
def login_for_access_token(
        form_data: OAuth2PasswordRequestForm = Depends(OAuth2PasswordRequestForm),
        service: TokenServices = Depends(TokenServices)
):
    return service.get_user_token(form_data=form_data)