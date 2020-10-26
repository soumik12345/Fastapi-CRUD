from starlette.testclient import TestClient

from backend.main import backend

client = TestClient(backend)


def test_ping():
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"ping": "pong!"}
