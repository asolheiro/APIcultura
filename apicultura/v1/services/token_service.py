from sqlalchemy import select
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends

from apicultura.core.models.user_model import User
from apicultura.core.database import Session
from apicultura.core.dependencies import get_db
from apicultura.core.exceptions import CredentialsException
from apicultura.core.security.token import crete_access_token
from apicultura.core.security.password_hash import verify_password


class TokenServices:
    def __init__(
        self,
        form_data: OAuth2PasswordRequestForm = Depends(
            OAuth2PasswordRequestForm
        ),
        db: Session = Depends(get_db),
    ) -> None:
        self.db = db
        self.form_data = form_data

    def get_user_token(self, form_data: OAuth2PasswordRequestForm):
        """Create an access token for an existing user"""

        user_db = self.db.scalar(
            select(User).where(User.email == self.form_data.username)
        )

        if not user_db:
            raise CredentialsException("User not found")
        if not verify_password(form_data.password, user_db.password):
            raise CredentialsException("Incorrect password")

        access_token = crete_access_token(data={"sub": user_db.email})
        return {"access_token": access_token, "token_type": "bearer"}
