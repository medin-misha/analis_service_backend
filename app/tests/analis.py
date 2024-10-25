from .fixtures import database, client
import random
from httpx import Response


def test_create_analis(database):
    user_data: dict = {
        "name": f"{random.random()}",
        "age": 16,
        "weight": 65,
        "gender": True,
    }
    create_user_response: Response = database.post("/users", json=user_data)
    assert create_user_response.status_code == 200
    analis: dict = {
        "name": "ПСА (PSA) - коефіцієнт",
        "unit": "%",
        "user_id": create_user_response.json().get("id"),
    }
    response: Response = database.post("/analis", json=analis)
    assert response.status_code == 200
    assert response.json().get("id")


def test_get_analis_list(database):
    response: Response = database.get("/analis")
    assert response.status_code == 200
    assert len(response.json()) != 0


def test_get_analis(database):
    analis_id: int = 1
    response: Response = database.get(f"/analis/{analis_id}")
    assert response.status_code == 200
    assert response.json().get("id")


def test_get_analis_by_name_and_user_id(database):
    analis_id: int = 1
    response_get_analis_by_id: Response = database.get(f"/analis/{analis_id}")
    assert response_get_analis_by_id.status_code == 200

    analis_name: str = response_get_analis_by_id.json().get("name")
    user_id: int = response_get_analis_by_id.json().get("id")

    response: Response = database.get(f"/analis/name/{analis_name}/{user_id}")
    assert response.status_code == 200
    assert response.json().get("id")


def test_delete_analis(database):
    analis_id: int = 1
    delete_response: Response = database.delete(f"/analis/{analis_id}")
    get_response: Response = database.get(f"/analis/{analis_id}")

    assert delete_response.status_code == 204
    assert get_response.status_code == 404
