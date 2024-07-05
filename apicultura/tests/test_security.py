from jwt import decode

from apicultura.core.security import crete_access_token
from apicultura.core.settings import Settings

def test_jwt():
    data = {'test': 'test'}
    token = crete_access_token(data)

    decoded = decode(
        token, 
        Settings().SECRET_KEY, 
        algorithms=Settings().ALGORITHM
        )
    
    assert decoded['test'] == data['test']
    assert decoded['exp']