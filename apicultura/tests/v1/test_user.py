from http import HTTPStatus

PATH = '/v1/users'


def test_create_user(client):
    data = {
        'username': 'karl',
        'email': 'karl@example.com',
        'password': 'secret',
    }

    response = client.post(
        PATH,
        json=data,
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {
        'username': data['username'],
        'email': data['email'],
        'id': 1,
    }

def test_read_user_successful(client):
    url = PATH + str(1)
    response = client.get(
        url
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'karl',
        'email': 'karl@example.com',
        'id': 1
    }

def test_list_users_successful(client):
    url = PATH + "/view"
    response = client.get(
        url
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() is not None


def test_update_user_successful(client):
    data = {
        'username': 'Pep'
    }
    url = PATH + str(1)
    
    response = client.put(
        url,
        json=data
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': data['username'],
        'email': 'karl@example.com',
        'id': 1
    }

def test_update_user_unsuccessful_404(client):
    data = {
        'username': 'Pep'
    }
    url = PATH + str(42)
    
    response = client.put(
        url,
        json=data
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {"details": "User not found"}


def test_delete_usersuccessful(client):
    url = PATH + str(1)

    response = client.delete(
        url
    )

    assert response.status_code == HTTPStatus.NO_CONTENT
    assert response.json() is None


def test_delete_user_unsuccessful_404(client):
    url = PATH + str(42)
    
    response = client.put(
        url
        )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {"details": "User not found"}