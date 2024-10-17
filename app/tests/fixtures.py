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
    analis_data: dict = {"name": "ПСА (PSA) - коефіцієнт", "unit": "%"}
    analis_value_data: dict = {
        "user_id": 1,
        "analis_id": 1,
        "value": "50",
        "date": "2024-10-19",
    }
    analis_standart_data: dict = {
        "analis_id": 1,
        "gender": True,
        "age_min": 0,
        "age_max": 10,
        "weight_min": 1,
        "weight_max": 35,
        "value": "3",
    }

    user_create_response: Response = client.post("/users", json=user_data)
    analis_create_response: Response = client.post("/analis", json=analis_data)
    # analis_standart_create_response: Response = client.post(
    #     "/analis/standart/", json=analis_standart_data
    # )
    analis_value_create_response: Response = client.post(
        "analis/value/", json=analis_value_data
    )

    assert user_create_response.status_code == 200
    assert analis_create_response.status_code == 200
    # assert analis_standart_create_response.status_code == 200
    assert analis_value_create_response.status_code == 200
    return client


@pytest.fixture
def database_schedule(client):
    user_data: dict = {"name": "misha", "age": 16, "weight": 65, "gender": True}
    analis_data: dict = {"name": "ПСА (PSA) - коефіцієнт", "unit": "%"}

    user_create_response: Response = client.post("/users", json=user_data)
    analis_create_response: Response = client.post("/analis", json=analis_data)

    assert user_create_response.status_code == 200
    assert analis_create_response.status_code == 200

    analis_values_data: list[dict] = [
        {
            "user_id": user_create_response.json().get("id"),
            "analis_id": analis_create_response.json().get("id"),
            "value": "50",
            "date": "2024-10-01",
        },
        {
            "user_id": user_create_response.json().get("id"),
            "analis_id": analis_create_response.json().get("id"),
            "value": "51",
            "date": "2024-10-02",
        },
        {
            "user_id": user_create_response.json().get("id"),
            "analis_id": analis_create_response.json().get("id"),
            "value": "53",
            "date": "2024-10-03",
        },
        {
            "user_id": user_create_response.json().get("id"),
            "analis_id": analis_create_response.json().get("id"),
            "value": "45",
            "date": "2024-10-04",
        },
        {
            "user_id": user_create_response.json().get("id"),
            "analis_id": analis_create_response.json().get("id"),
            "value": "48",
            "date": "2024-10-05",
        },
        {
            "user_id": user_create_response.json().get("id"),
            "analis_id": analis_create_response.json().get("id"),
            "value": "55",
            "date": "2024-10-06",
        },
        {
            "user_id": user_create_response.json().get("id"),
            "analis_id": analis_create_response.json().get("id"),
            "value": "43",
            "date": "2024-10-07",
        },
        {
            "user_id": user_create_response.json().get("id"),
            "analis_id": analis_create_response.json().get("id"),
            "value": "45",
            "date": "2024-10-08",
        },
        {
            "user_id": user_create_response.json().get("id"),
            "analis_id": analis_create_response.json().get("id"),
            "value": "50",
            "date": "2024-10-09",
        },
    ]

    for analis_value_data in analis_values_data:
        analis_value_create_response: Response = client.post(
            "analis/value/", json=analis_value_data
        )
        assert analis_value_create_response.status_code == 200

    return (client, user_create_response.json(), analis_create_response.json())
