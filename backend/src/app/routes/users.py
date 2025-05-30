from http import HTTPStatus

from fastapi import APIRouter

from app.schemas.users import UserCreateSchema, UserDBSchema, UserPublicSchema

router = APIRouter()

dataBase = []


@router.post(
    '/users', response_model=UserPublicSchema, status_code=HTTPStatus.CREATED
)
def create_user(user: UserCreateSchema):
    user_with_id = UserDBSchema(
        **user.model_dump(),
        id=len(dataBase) + 1,
    )
    dataBase.append(user_with_id)
    return user_with_id


@router.get(
    '/users', response_model=list[UserPublicSchema], status_code=HTTPStatus.OK
)
def get_users():
    return dataBase
