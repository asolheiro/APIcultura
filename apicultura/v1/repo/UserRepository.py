from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from apicultura.core.dependencies import get_db
from apicultura.core.exceptions import DuplicatedRegister, NotFoundException
from apicultura.core.models.user_model import User
from apicultura.core.schemas.user_schema import UserIn
from apicultura.core.security.password_hash import get_password_hash


class UserRepository:
    db: Session
    _model = User

    def __init__(self, db: Session = Depends(get_db)) -> None:
        self.db = db

    @property
    def base_query(self):
        return (
            self.db.query(self._model)
            .filter(self._model.deleted_at.is_(None))
            .order_by(self._model.created_at.asc())
        )

    def get_by_id(self, pk: int) -> User:
        return self.base_query.filter_by(id=pk).first()

    def get_by_username_or_email(self, username: str, email: str) -> User:
        user = self.db.scalar(
            select(User).where(
                (User.username == username) | (User.email == email)
            )
        )

        return user

    def list_and_filter_users(self, limit: int, skip: int):
        query = self.base_query
        return query.offset(skip).limit(limit).all()

    def create(self, user: UserIn) -> User:
        self.db.add(user)
        try:
            self.db.commit()
        except IntegrityError as exc:
            self.db.rollback()
            raise DuplicatedRegister(model=self._model) from exc

        self.db.refresh(user)
        return user

    def update(self, user_id: int, **updated_values) -> User:
        db_user = self.db.scalar(select(User).where(User.id == user_id))
        if not db_user:
            raise NotFoundException("User not found")

        for key, value in updated_values.items():
            if key == 'password':
                return get_password_hash(value)
            setattr(db_user, key, value)

        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)

        return db_user

    def delete(self, user_id: int) -> User:
        user = self.db.scalar(select(User).where(User.id == user_id))
        if not user:
            raise NotFoundException("User not found")

        self.db.delete(user)
        self.db.commit()

        return "ok"
