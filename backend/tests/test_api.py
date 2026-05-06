import pytest
from fastapi.testclient import TestClient

from api.app import app


@pytest.fixture()
def client():
    with TestClient(app) as client:
        yield client


def test_health_endpoint(client: TestClient):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_parse_cv_missing_file(client: TestClient):
    response = client.post("/parse-cv")
    assert response.status_code == 422


def test_parse_cv_invalid_extension(client: TestClient):
    files = {"file": ("test.txt", b"Dummy content", "text/plain")}
    response = client.post("/parse-cv", files=files)
    assert response.status_code == 400
    assert "Unsupported file type" in response.json()["detail"]
