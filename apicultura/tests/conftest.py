import pytest
from fastapi.testclient import TestClient

from apicultura.v1.main import app


@pytest.fixture()
def client():
    return TestClient(app)
