from fastapi import HTTPException, status


class BadRequestException(HTTPException):
    def __init__(self, details: str) -> None:
        super().__init__(status.HTTP_400_BAD_REQUEST, details)


class NotFoundException(HTTPException):
    def __init__(self, details: str) -> None:
        super().__init__(status.HTTP_404_NOT_FOUND, details)


class DuplicatedRegister(HTTPException):
    def __init__(self, model) -> None:
        super().__init__(
            status.HTTP_409_CONFLICT,
            f"Duplicated register on {model.__name__}",
        )

class CredentialsException(HTTPException):
    def __init__(
            self, 
            headers,
            details='Could not validate credentials') -> None: 
        super().__init__(
            status.HTTP_401_UNAUTHORIZED,
            details,
            headers={'WWW-Authenticate': 'Bearer'}
        )
