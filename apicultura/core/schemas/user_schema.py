from pydantic import BaseModel, ConfigDict, EmailStr


class UserIn(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr

    model_config = ConfigDict(from_attributes=True)


class UserUpdate(BaseModel):
    username: str | None = None
    email: EmailStr | None = None
    password: str | None = None


class UsersList(BaseModel):
    users: list[UserOut]

    model_config = ConfigDict(from_attributes=True)
