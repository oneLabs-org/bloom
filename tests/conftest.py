import pytest
from fastapi.testclient import TestClient
from bloom.app import app


@pytest.fixture(scope="module")
def test_app():
    client = TestClient(app=app)
    yield client
