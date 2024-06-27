from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from apicultura.core.dependencies import get_db
from apicultura.core.exceptions import DuplicatedRegister, NotFoundException
<<<<<<< HEAD
from apicultura.core.models.user_model import User
from apicultura.core.schemas.user_schema import UserIn
=======
from apicultura.core.models.user import User
from apicultura.core.schemas.user import UserIn
>>>>>>> a694a75 (Primeira migração com alembic. Adicionando a tabela users)


class UserRepository:
    db: Session
    _model = User

    def __init__(self, db: Session = Depends(get_db)) -> None:
        self.db = db

    @property
    def base_query(self):
        return self.db.query(
            self._model.filter(self._model.deleted_at.is_(None))
        )

    def get_by_id(self, pk: int) -> User:
        user = self.base_query.filter_by(id=pk).first()
        if not user:
            raise NotFoundException('User not found')

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
            raise NotFoundException('User not found')

        for key, value in updated_values.items():
            setattr(db_user, key, value)

        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)

        return db_user

    def delete(self, user_id: int) -> User:
        user = self.db.scalar(select(User).where(User.id == user_id))
        if not user:
            raise NotFoundException('User not found')

        self.db.delete(user)
        self.db.commit()

        return 'ok'
