from datetime import datetime, timedelta

from jwt import encode
from pwdlib  import PasswordHash
from zoneinfo import ZoneInfo
from apicultura.core.settings import Settings


settings = Settings()

pwd_context = PasswordHash.recommended()


def crete_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(tz=ZoneInfo("UTC")) + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    to_encode.update({'exp': expire})
    encode_jwt = encode(
        to_encode, 
        settings.SECRET_KEY, 
        algorithm=settings.ALGORITHM
        )
    
    return encode_jwt


