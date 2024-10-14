from .fixtures import database, client
from httpx import Response


def test_create_analis(database):
    analis: dict = {"name": "ПСА (PSA) - коефіцієнт", "unit": "%"}
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


def test_delete_analis(database):
    analis_id: int = 1
    delete_response: Response = database.delete(f"/analis/{analis_id}")
    get_response: Response = database.get(f"/analis/{analis_id}")

    assert delete_response.status_code == 204
    assert get_response.status_code == 404
