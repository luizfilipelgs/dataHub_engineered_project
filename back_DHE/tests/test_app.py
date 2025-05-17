from http import HTTPStatus

from fastapi.testclient import TestClient

from src.back_dhe.app import app

client = TestClient(app)


def test_hello_world():
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Hello World!!!'}
