from http import HTTPStatus


def test_read_root_succeed(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'APIcultura v1.'}
