from pydantic import BaseModel, ConfigDict

class TokenOut(BaseModel):
    access_token: str
    token_type: str

    model_config = ConfigDict(from_attributes=True)

class TokenData(BaseModel):
    username: str | None = None