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


def test_list_5_tasks_successfull(client, user, token):
    url = PATH
    TaskFactory.create_batch(5, user_id=user["id"])
    print(url)
    response = client.get(
        url,
        headers = {
            'Authorization': f"Bearer {token}"
        }
    )

    assert len(response.json()['Tasks']) == 5

def test_list_pagination_successful(client, user, token):
    offset = 1
    limit = 2
    url = PATH + f"?offset={offset}&limit={limit}"
    TaskFactory.create_batch(5, user_id=user['id'])

    response = client.get(
        url,
        headers = {
            'Authorization': f'Bearer {token}'
        }
    )

    assert response.status_code == HTTPStatus.OK    
    assert len(response.json()['Tasks']) == 2


def test_list_title_filter_successfull(client, user, token):
    filter = "Test"
    url = PATH + f"?title={filter}"
    TaskFactory(user_id=user['id'], title='title filter Test')

    response = client.get(
        url,
        headers = {
            'Authorization': f'Bearer {token}'
        }
    )    

    assert response.status_code == HTTPStatus.OK
    assert len(response.json()['Tasks']) == 1


def test_list_description_filter_successfull(client, user, token):
    filter = "Test"
    url = PATH + f"?description={filter}"
    TaskFactory(user_id=user['id'], description='description filter Test')

    response = client.get(
        url,
        headers = {
            'Authorization': f'Bearer {token}'
        }
    )    

    assert response.status_code == HTTPStatus.OK
    assert len(response.json()['Tasks']) == 1


def test_list_state_filter_successfull(client, user, token):
    filter = "draft"
    url = PATH + f"?state={filter}"
    TaskFactory(user_id=user['id'], state='draft')

    response = client.get(
        url,
        headers = {
            'Authorization': f'Bearer {token}'
        }
    )    

    assert response.status_code == HTTPStatus.OK
    assert len(response.json()['Tasks']) == 1


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
