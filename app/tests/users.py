from httpx import Response
from .fixtures import client, database


def test_create_client(database):
    user_data: dict = {"name": "misha", "age": 16, "weight": 65, "gender": True}

    response: Response = database.post("/users", json=user_data)
    assert response.status_code == 200
    assert response.json().get("id")


def test_get_clients_list(database):
    response: Response = database.get("/users")
    assert response.status_code == 200
    assert isinstance(response.json(), list) == True
    assert len(response.json()) != 0


def test_get_client(database):
    user_id: int = 1
    response: Response = database.get(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.json().get("id")


def test_get_client_by_name(database):
    user_id: int = 1
    response_get_by_id: Response = database.get(f"/users/{user_id}")
    assert response_get_by_id.status_code == 200

    name: str = response_get_by_id.json().get("name")
    response: Response = database.get(f"/users/name/{name}")
    assert response.status_code == 200
    assert response.json().get("id")


def test_patch_client(database):
    value: dict = {"gender": False}
    user_id: int = 1
    response: Response = database.patch(f"/users/{user_id}", json=value)
    assert response.status_code == 200
    assert response.json().get("gender") is value.get("gender")


def test_delete_user(database):
    user_id: int = 1
    response: Response = database.delete(f"/users/{user_id}")
    assert response.status_code == 204
