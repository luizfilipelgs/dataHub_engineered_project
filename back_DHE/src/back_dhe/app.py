from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from back_dhe.schemas import Message

app = FastAPI()


@app.get('/', response_model=Message, status_code=HTTPStatus.OK)
def hello_world():
    return {'message': 'Hello World!!!'}


@app.get('/olamundo', response_class=HTMLResponse, status_code=HTTPStatus.OK)
def hello_world_pag():
    return """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta
                name="viewport"
                content="width=device-width,
                initial-scale=1.0"
            >
            <title>Hello World</title>
        </head>
        <body>
            <h1>Hello World!!!</h1>
        </body>
        </html>
    """
