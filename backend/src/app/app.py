from http import HTTPStatus

from fastapi import FastAPI

from app.routes import users
from app.schemas.schemas import Message

app = FastAPI()


app.include_router(users.router, tags=['Users'])


@app.get('/health', response_model=Message, status_code=HTTPStatus.OK)
def health_check():
    return {'message': 'OK'}
