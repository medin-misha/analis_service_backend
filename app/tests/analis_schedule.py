from .fixtures import database_schedule, client
from httpx import Response


def test_analis_schedule(database_schedule):
    client = database_schedule[0]
    user = database_schedule[1]
    analis = database_schedule[2]

    user_and_analis_id: dict = {"user_id": user["id"], "analis_id": analis["id"]}
    response: Response = client.post("/schedule/", json=user_and_analis_id)
    assert response.status_code == 200
    assert response.headers.get("content-type") == "image/png"


def test_analis_schedule_not_found_user(database_schedule):
    client = database_schedule[0]
    user_and_analis_id: dict = {"user_id": 12, "analis_id": 1}
    response: Response = client.post("/schedule/", json=user_and_analis_id)
    assert response.status_code == 404


def test_analis_schedule_not_found_analis(database_schedule):
    client = database_schedule[0]
    user_and_analis_id: dict = {"user_id": 1, "analis_id": 21}
    response: Response = client.post("/schedule/", json=user_and_analis_id)
    assert response.status_code == 404


def test_analis_schedule_bad_data(database_schedule):
    user: dict = database_schedule[1]
    analis: dict = database_schedule[2]

    client = database_schedule[0]
    user_and_analis_id: dict = {"user_id": user["id"], "analis_id": analis["id"]}
    bad_analis_value_data: dict = {
        "user_id": user["id"],
        "analis_id": analis["id"],
        "value": "пиздец в место значения",
        "date": "2024-10-09",
    }
    analis_value_create_response: Response = client.post(
        "analis/value/", json=bad_analis_value_data
    )
    response: Response = client.post("/schedule/", json=user_and_analis_id)

    assert analis_value_create_response.status_code == 200
    assert response.status_code == 409
