from fastapi.testclient import TestClient
from httpx import Response
import pytest
import main


@pytest.fixture
def client():
    test_client = TestClient(app=main.app)
    response: Response = test_client.get("/make-test-db")
    assert response.status_code == 200
    return test_client


@pytest.fixture
def database(client):
    user_data: dict = {"name": "misha", "age": 16, "weight": 65, "gender": True}
    user_create_response: Response = client.post("/users", json=user_data)


    assert user_create_response.status_code == 200
    assert user_create_response.json().get("id")
    return client