from pydantic import BaseModel, ConfigDict, EmailStr


class UserIn(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserDB(UserIn):
    id: int


class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr

    model_config = ConfigDict(from_attributes=True)


class UserUpdate(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserList(BaseModel):
    users: list[UserOut]
