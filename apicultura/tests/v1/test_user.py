from http import HTTPStatus

from apicultura.tests.factories.user_factory import UserFactory
from apicultura.core.schemas import user_schema

PATH = "/v1/users/"

# TESTS TO CREATE ENDPOINT
def test_successful_create_user(client):
    data = {
        "username": "karl",
        "email": "karl@example.com",
        "password": "secret",
    }

    response = client.post(
        PATH,
        json=data,
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        "username": data["username"],
        "email": data["email"],
        "id": 1,
    }


def test_unsuccessful400_creat_existing_username(client):
    user = UserFactory()

    data = {
        'username': 'karl',
        'email': user.email,
        'password': 'secret'
    }
    response = client.post(
        PATH,
        json=data
    )

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json() == {'detail': 'Email already exists on database'}

def test_unsuccessful400_creat_existing_email(client):
    user = UserFactory()

    data = {
        'username': user.username,
        'email': 'karl@pep.com',
        'password': 'secret'
    }
    response = client.post(
        PATH,
        json=data
    )

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json() == {'detail': 'Username already exists on database'}

# TESTS TO READ ENDPOINTS
def test_read_user_successful(client):
    user = UserFactory(username="Karl", password="Pep", email="karl@pep.com")

    url = PATH + str(user.id)

    response = client.get(url)

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "username": user.username,
        "email": user.email,
        "id": user.id,
    }


def test_list_users_successful(client):
    users =  UserFactory.create_batch(5)
    users_schema = {'users': [user_schema.UserOut.model_validate(user).model_dump() for user in users]}

    url = PATH + "view/"
    response = client.get(url)

    assert response.status_code == HTTPStatus.OK
    assert response.json() == users_schema


# TESTS TO UPDATE ENDPOINT
def test_update_user_successful(client):
    user = UserFactory()
    data = {"username": "Karl"}

    url = PATH + str(user.id)

    response = client.put(url, json=data)

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "username": data["username"],
        "email": user.email,
        "id": user.id,
    }


def test_update_user_unsuccessful_404(client):
    data = {"username": "Pep"}
    url = PATH + str(42)

    response = client.put(url, json=data)

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {"detail": "User not found"}


# TESTS TO DELETE ENDPOINT
def test_delete_user_successful(client):
    user = UserFactory()
    url = PATH + str(user.id)

    response = client.delete(url)

    assert response.status_code == HTTPStatus.NO_CONTENT


def test_delete_user_unsuccessful_404(client):
    url = PATH + str(42)

    response = client.delete(url)

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {"detail": "User not found"}
