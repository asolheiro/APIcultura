from fastapi import Depends

from apicultura.core.exceptions import NotFoundException
<<<<<<< HEAD
from apicultura.core.schemas.user_schema import UserDB, UserIn, UserUpdate
=======
from apicultura.core.schemas.user import UserDB, UserIn, UserUpdate
>>>>>>> a694a75 (Primeira migração com alembic. Adicionando a tabela users)
from apicultura.v1.repo.UserRepository import UserRepository


class UserServices:
    def __init__(self, repo: UserRepository = Depends(UserRepository)) -> None:
        self.repo = repo

    def get_user(self, user_id: int):
        user = self.repo.get_by_id(pk=user_id)
        if not user:
            raise NotFoundException('User not found')

        return user

    def list_users(self):
        return self.repo.base_query

    def create_user(self, user_input: UserIn):
        user_with_id = UserDB(
            **user_input.model_dump(), id=len(self.database) + 1
        )
        self.database.append(user_with_id)

        return user_with_id

    def update_user(self, user_id: int, user_update: UserUpdate):
        db_user = self.repo.get_by_id(pk=user_id)
        if not user_id:
            raise NotFoundException('User not found')

        updated_values = user_update.model_dump(exclude_unset=True)
        db_user = self.repo.update(pk=user_id, **updated_values)

        return db_user

    def delete_user(self, user_id: int):
        user = self.get_user(user_id=user_id)
        if not user:
            raise NotFoundException('User not found')

        self.repo.delete(user_id=user_id)

        return 'ok'
