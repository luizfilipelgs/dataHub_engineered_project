from pydantic import BaseModel, EmailStr


class UserPublicSchema(BaseModel):
    username: str
    email: EmailStr
    id: int


class UserCreateSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserDBSchema(UserCreateSchema):
    id: int
