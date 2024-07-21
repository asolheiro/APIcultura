from http import HTTPStatus
from jwt import decode

from freezegun import freeze_time

from apicultura.core.security.token import crete_access_token
from apicultura.core.settings import Settings

# from apicultura.core.security.password_hash import get_password_hash


## Test to CREATE token
def test_create_jwt_token():
    data = {"test": "test"}
    token = crete_access_token(data)

    decoded = decode(
        token, Settings().SECRET_KEY, algorithms=Settings().ALGORITHM
    )

    assert decoded["test"] == data["test"]
    assert decoded["exp"]


## Test to GET tokens
def test_get_token(client, user):
    response = client.post(
        url="/v1/auth/",
        data={
            "username": user["email"],
            "password": user["password"],
            "content-type": "multipart/form-data",
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert "access_token" in response.json()
    assert "token_type" in response.json()


def test_get_token_unsuccesfull(client):
    response = client.post(
        "/v1/auth/",
        data={
            "username": "Pep@karl.com",
            "password": "PepKarl",
            "content-type": "multipart/form-data",
        },
    )

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {"detail": "User not found"}


def test_get_token_unsuccesfull_wrong_password(client, user):
    response = client.post(
        "/v1/auth/",
        data={
            "username": user["email"],
            "password": "KarlPep",
            "content-type": "multipart/form-data",
        },
    )

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {"detail": "Incorrect password"}


def test_refresh_token(client, user, token):
    response = client.post(
        "v1/auth/refresh/",
        headers={"Authorization": f"Bearer {token}"},
    )

    data = response.json()

    assert response.status_code == HTTPStatus.OK
    assert "access_token" in data
    assert "token_type" in data
    assert data["token_type"] == "bearer"


def test_token_expired_after_time(client, user):
    with freeze_time("2024-07-16 13:20"):
        response = client.post(
            "v1/auth/",
            data={
                "username": user["email"],
                "password": "ItsASecret",
                "content-type": "multipart/form-data",
            },
        )

        assert response.status_code == HTTPStatus.OK
        token = response.json()["access_token"]

    with freeze_time("2024-07-16 14:51"):
        response = client.put(
            f"/v1/users/{user['id']}",
            headers={"Authorization": f"Bearer {token}"},
            json={
                "username": "wrongwrong",
                "email": "wrong@wrong.com",
                "password": "wrong",
            },
        )

        assert response.status_code == HTTPStatus.UNAUTHORIZED
        assert response.json() == {"detail": "Could not validate credentials"}


def test_token_expired_dont_refresh(client, user):
    with freeze_time("2024-07-16 13:51:00"):
        response = client.post(
            "v1/auth/",
            data={
                "username": user["email"],
                "password": user["password"],
                "content-type": "multipart/form-data",
            },
        )
        assert response.status_code == HTTPStatus.OK
        token = response.json()["access_token"]

    with freeze_time("2024-07-16 14:21:00"):
        response = client.post(
            "v1/auth/refresh",
            headers={"Authorization": f"Bearer {token}"},
        )
        assert response.status_code == HTTPStatus.UNAUTHORIZED
        assert response.json() == {"detail": "Could not validate credentials"}

