from datetime import datetime


from sqlalchemy.orm import Mapped, mapped_column

from apicultura.core.models.base import BModel


class User(BModel):
    __tablename__ = 'users'

    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
