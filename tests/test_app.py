from http import HTTPStatus

from fastapi.testclient import TestClient

from apicultura.app import app


def test_read_root_succeed():
    client = TestClient(app)

    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'APIcultura v1.'}
