from http import HTTPStatus
from jwt import decode

from apicultura.core.security.token import crete_access_token
from apicultura.core.settings import Settings



def test_create_jwt_token():
    data = {'test': 'test'}
    token = crete_access_token(data)

    decoded = decode(
        token, 
        Settings().SECRET_KEY, 
        algorithms=Settings().ALGORITHM
        )
    
    assert decoded['test'] == data['test']
    assert decoded['exp']

def test_get_token(client, user):
    response = client.post(
        url='/v1/token/',
        data={
            'username': user['email'],
            'password': user['password'],
            'content-type': 'multipart/form-data'
    }
    )

    assert response.status_code == HTTPStatus.OK 
    assert 'access_token' in response.json()
    assert 'token_type' in response.json()