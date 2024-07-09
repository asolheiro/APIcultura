from fastapi import Depends

from apicultura.core.exceptions import BadRequestException, NotFoundException
from apicultura.core.models.user_model import User
from apicultura.core.security.password_hash import get_password_hash
from apicultura.core.schemas.user_schema import UserIn, UserUpdate
from apicultura.v1.repo.UserRepository import UserRepository


class UserServices:
    def __init__(self, repo: UserRepository = Depends(UserRepository)) -> None:
        self.repo = repo

    def get_user_by_id(self, user_id: int):
        """View and existing user"""
        user = self.repo.get_by_id(pk=user_id)
        if not user:
            raise NotFoundException("User not found")
        return user

    def list_users(self, limit: int, skip: int):
        """View all users"""
        users = self.repo.list_and_filter_users(limit=limit, skip=skip)

        return users

    def create_user(self, user_input: UserIn):
        """Crate a new user"""
        if db_user := self.repo.get_by_username_or_email(
            username=user_input.username, email=user_input.email
        ):
            if db_user.username == user_input.username:
                raise BadRequestException(
                    "Username already exists on database"
                )
            elif db_user.email == user_input.email:
                raise BadRequestException(
                    "Email already exists on database"
                    )
    
        db_user = User(
            email = user_input.email,
            username = user_input.username,
            password=get_password_hash(user_input.password)
        )
        
        return self.repo.create(user=db_user)

    def update_user(self, user_id: int, user_update: UserUpdate, current_user: User):
        """Update an existing user"""

        if current_user.id != user_id:
            raise BadRequestException('Not enough permissions')
        
        db_user = self.repo.get_by_id(pk=user_id)
        if not user_id:
            raise NotFoundException("User not found")

        updated_values = user_update.model_dump(exclude_unset=True)
        db_user = self.repo.update(user_id=user_id, **updated_values)

        return db_user

    def delete_user(self, user_id: int, current_user: User):
        """Delete and existing user"""
        
        if current_user.id != user_id:
            raise BadRequestException('Not enough permissions')
        
        user = self.get_user_by_id(user_id=user_id)
        if not user:
            raise NotFoundException("User not found")

        self.repo.delete(user_id=user_id)

        return "ok"
