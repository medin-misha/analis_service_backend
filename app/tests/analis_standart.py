from .fixtures import database, client
from httpx import Response


def test_create_analis_standart(database):
    analis_standart_data: dict = {
        "analis_id": 1,
        "gender": True,
        "age_min": 0,
        "age_max": 10,
        "weight_min": 1,
        "weight_max": 35,
        "value": "3",
    }
    response: Response = database.post("/analis/standart/", json=analis_standart_data)
    assert response.json().get("id")
    assert response.status_code == 200


def test_get_all_analis_standarts(database):
    response: Response = database.get("/analis/standart/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_analis_standart(database):
    analis_standart_id: int = 1
    response: Response = database.get(f"/analis/standart/{analis_standart_id}")
    assert response.status_code == 200
    assert response.json().get("id")


def test_patch_analis_standart(database):
    analis_standart_id: int = 1
    analis_standart_value: dict = {
        "gender": False,
    }
    response: Response = database.patch(
        f"/analis/standart/{analis_standart_id}", json=analis_standart_value
    )
    assert response.status_code == 200
    assert response.json().get("gender") == analis_standart_value.get("gender")


def test_delete_analis_standart(database):
    analis_standart_id: int = 1
    response: Response = database.delete(f"/analis/standart/{analis_standart_id}")
    get_response: Responsee = database.get(f"/analis/standart/{analis_standart_id}")
    assert response.status_code == 204
    assert get_response.status_code == 404
