from http import HTTPStatus

from fastapi.testclient import TestClient

from src.back_dhe.app import app

client = TestClient(app)


def test_hello_world():
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Hello World!!!'}


def test_hello_world_pag():
    response = client.get('/olamundo')

    assert response.status_code == HTTPStatus.OK
    assert '<h1>Hello World!!!</h1>' in response.text
