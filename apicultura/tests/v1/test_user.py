from http import HTTPStatus


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


def test_unsuccessful400_creat_existing_username(client, user):
    data = {"username": "karl", "email": user["email"], "password": "secret"}
    response = client.post(PATH, json=data)

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json() == {"detail": "Username already exists on database"}


def test_unsuccessful400_creat_existing_email(client, user):
    data = {
        "username": user["username"],
        "email": "karl@pep.com",
        "password": "secret",
    }
    response = client.post(PATH, json=data)

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json() == {"detail": "Username already exists on database"}


# TESTS TO READ ENDPOINTS


def test_read_user_successful(client, user):
    url = PATH + str(user["id"])

    response = client.get(url)

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "username": user["username"],
        "email": user["email"],
        "id": user["id"],
    }


def test_list_users_successful(client, users):
    users_schema = {
        "users": [
            user_schema.UserOut.model_validate(user).model_dump()
            for user in users
        ]
    }

    url = PATH + "view/"
    response = client.get(url)

    assert response.status_code == HTTPStatus.OK
    assert response.json() == users_schema


# TESTS TO UPDATE ENDPOINT
def test_update_user_successful(client, user, token):
    data = {"username": "Karl"}

    url = PATH + str(user["id"])

    response = client.put(
        url=url,
        headers={"Authorization": f"Bearer {token}"},
        json=data,
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "username": data["username"],
        "email": user["email"],
        "id": user["id"],
    }


def test_update_user_unsuccessful_404(client, token):
    data = {"username": "Pep"}
    url = PATH + str(42)

    response = client.put(
        url, headers={"Authorization": f"Bearer {token}"}, json=data
    )

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {"detail": "Not enough permissions"}


def test_update_user_unseccessful_401(client, token, user_2):
    response = client.put(
        PATH + str(user_2["id"]),
        json={"username": "update_test"},
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {"detail": "Not enough permissions"}


# TESTS TO DELETE ENDPOINT
def test_delete_user_successful(client, user, token):
    url = PATH + str(user["id"])

    response = client.delete(url, headers={"Authorization": f"Bearer {token}"})

    assert response.status_code == HTTPStatus.NO_CONTENT


def test_delete_user_unsuccessful_404(client, token):
    url = PATH + str(42)

    response = client.delete(url, headers={"Authorization": f"Bearer {token}"})

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {"detail": "Not enough permissions"}
