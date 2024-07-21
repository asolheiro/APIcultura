from http import HTTPStatus

from apicultura.tests.factories.task_factory import TaskFactory


PATH = "/v1/task/"


# Tests to POST endpoint
def test_create_task(client, token):
    data = {
        "title": "Teste",
        "description": "Descrição",
        "state": "todo",
    }
    response = client.post(
        PATH,
        headers={"Authorization": f"Bearer {token}"},
        json=data,
    )

    assert response.status_code == HTTPStatus.CREATED
    assert "id" in response.json()


def test_create_task_unsuccessful_401(client):
    data = (
        {
            "title": "Teste",
            "description": "Descrição",
            "state": "todo",
        },
    )
    response = client.post(PATH, json=data)

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {"detail": "Not authenticated"}


def test_create_task_unsuccessful_authentication_401(client):
    data = {
        "title": "Teste",
        "description": "Descrição",
        "state": "todo",
    }
    response = client.post(
        PATH, json=data, headers={"Authorization": "Bearer 42"}
    )

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {"detail": "Could not validate credentials"}


def test_create_task_unsuccessful_422(client, token):
    data = {
        "title": "Teste",
        "state": "todo",
    }

    response = client.post(
        PATH, json=data, headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY


# Tests to GET endpoints
def test_get_task(client, user, token):
    task = TaskFactory(user_id=user["id"])
    url = PATH + str(task.id)

    response = client.get(url, headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == HTTPStatus.OK
    assert "id" in response.json()


def test_get_task_unssuccesful_401(client, user):
    task = TaskFactory(user_id=user["id"])
    url = PATH + str(task.id)

    response = client.get(url)
    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {"detail": "Not authenticated"}


def test_get_task_authentication_unssuccesful_401(client, user):
    task = TaskFactory(user_id=user["id"])
    url = PATH + str(task.id)

    response = client.get(
        url,
        headers = {
            "Authorization": "Bearer 42"
        }
    )
    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {"detail": "Could not validate credentials"}

def test_get_task_not_found_unssuccesful_404(client, token):
    url = PATH + str(42)

    response = client.get(
        url,
        headers = {
            "Authorization": f"Bearer {token}"
        }
    )
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {"detail": "Task not found"}

# Test to PUT endpoint
def test_update_enpoint(client, user, token):
    task = TaskFactory(user_id=user["id"])
    url = PATH + str(task.id)
    data = {
        "title": "title update test"
    }

    response = client.put(
        url,
        json=data,
        headers = {
            "Authorization": f"Bearer {token}"
        }
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'id': 1}

def test_update_enpoint_field_forbidden_unsuccessfull(client, user, token):
    task = TaskFactory(user_id=user["id"])
    url = PATH + str(task.id)
    data = {
        "id": 42
    }

    response = client.put(
        url,
        json=data,
        headers = {
            "Authorization": f"Bearer {token}"
        }
    )
    response = client.get(
        url,
        headers = {
            "Authorization": f"Bearer {token}"
        }
    )
    assert response.json() == {'id': 1}

def test_delete_task_successfull(client, user, token):
    task = TaskFactory(user_id=user['id'])
    url = PATH + str(task.id)

    response = client.delete(
        url,
        headers = {
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == HTTPStatus.NO_CONTENT

def test_delete_task_not_found_unsuccessfull_404(client, token):
    url = PATH + "42"
    response = client.delete(
        url,
        headers = {
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == HTTPStatus.NOT_FOUND 
    assert response.json() == {'detail': 'Task not found'}

def test_delete_task_not_found_unsuccessfull_401(client, user):
    task = TaskFactory(user_id = user['id'])
    url = PATH + str(task.id)

    response = client.delete(
        url
    )

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'detail': 'Not authenticated'}
