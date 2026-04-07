from pydantic import BaseModel, Field


class LoginRequest(BaseModel):
    id_token: str = Field(min_length=1)


class LoginResponse(BaseModel):
    ok: bool = True

