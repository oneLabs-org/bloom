from fastapi.testclient import TestClient
from bloom.app import app

client = TestClient(app=app)


def test_health():
    response = client.get("/healthz")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
