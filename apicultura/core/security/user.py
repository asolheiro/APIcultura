from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jwt import DecodeError, decode, ExpiredSignatureError
from sqlalchemy import select
from sqlalchemy.orm import Session

from apicultura.core.exceptions import CredentialsException
from apicultura.core.database import get_session
from apicultura.core.models.user_model import User
from apicultura.core.schemas.token_schema import TokenData
from apicultura.core.settings import Settings


settings = Settings()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/")


async def get_current_user(
    session: Session = Depends(get_session),
    token: str = Depends(oauth2_scheme)
):
    try: 
        payload = decode(
            token, 
            settings.SECRET_KEY, 
            algorithms=[settings.ALGORITHM]
            )
        username: str = payload.get('sub')
        if not username:
            raise CredentialsException()
        token_data = TokenData(username=username)
    except DecodeError:
        raise CredentialsException("Could not validate credentials")
    except ExpiredSignatureError:
        raise CredentialsException("Could not validate credentials")
    
    user = session.scalar(
        select(User).where(User.email == token_data.username)
    )

    if user is None:
        raise CredentialsException("Could not validate credentials")
    
    return user