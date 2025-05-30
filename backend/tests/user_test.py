from http import HTTPStatus

from app.routes.users import dataBase


def test_create_user(client):
    response = client.post(
        '/users',
        json={
            'username': 'teste',
            'email': 'teste@email.com',
            'password': 'teste123',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'username': 'teste',
        'email': 'teste@email.com',
    }


def test_get_users(client):
    dataBase.clear()
    response = client.post(
        '/users',
        json={
            'username': 'teste',
            'email': 'teste@email.com',
            'password': 'teste123',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    response = client.get('/users')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == [
        {
            'id': 1,
            'username': 'teste',
            'email': 'teste@email.com',
        }
    ]
