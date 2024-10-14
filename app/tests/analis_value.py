from .fixtures import database, client
from httpx import Response


def test_create_analis_value(database):
    analis_value_data: dict = {"user_id": 1, "analis_id": 1, "value": "50"}
    response: Response = database.post("/analis/value/", json=analis_value_data)
    assert response.json().get("id")
    assert response.status_code == 200


def test_get_all_analis_value(database):
    response: Response = database.get("/analis/value/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_analis_value(database):
    analis_value_id: int = 1
    response: Response = database.get(f"analis/value/{analis_value_id}")
    assert response.status_code == 200
    assert response.json().get("id")


def test_patch_analis_value(database):
    analis_value_id: int = 1
    analis_value_patch: dict = {"value": "51"}
    response: Response = database.patch(
        f"/analis/value/{analis_value_id}", json=analis_value_patch
    )
    assert response.status_code == 200
    assert response.json().get("value") == analis_value_patch.get("value")


def test_delete_analis_value(database):
    analis_value_id: int = 1
    response: Response = database.delete(f"/analis/value/{analis_value_id}")
    get_response: Response = database.get(f"/analis/value/{analis_value_id}")
    assert response.status_code == 204
    assert get_response.status_code == 404
