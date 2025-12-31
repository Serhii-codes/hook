import requests
from datetime import datetime, timezone



# Task: Testing SpaceX Launches API with a filter.
# Endpoint:
# https://api.spacexdata.com/v4/launches/query
# Requirements:
# Send a POST request with a JSON body to get only launches from 2020.
# Verify:
# status code is 200
# the field docs is a non-empty list
# each launch has keys: "name", "date_utc", "success"
# "date_utc" can be converted to a datetime object
# "success" is True, False, or None
# Extra: check that "date_utc" belongs to the year 2020 for all results.

ENDPOINT = "https://api.spacexdata.com/v4/launches/query"

# Фільтр на 2020 рік
def launches_2020():
    payload = {
        "query": {
            "date_utc": {
                "$gte": "2020-01-01T00:00:00.000Z",
                "$lt": "2021-01-01T00:00:00.000Z"
            }
        },
        "options": {"limit": 50}                         # обмеження по кількості
    }
    response = requests.post(ENDPOINT, json=payload)
    response.raise_for_status() # перевірка на помилку
    data = response.json()
    return data



def test_code_launches():
    result = launches_2020()
    assert "docs" in result



def test_docs():
    result = launches_2020()
    assert "docs" in result
    assert isinstance(result["docs"], list)
    assert len(result["docs"]) > 0

def test_launches_key():
    result = launches_2020()
    for launch in result["docs"]:
        for key in ["name", "date_utc", "success"]:
            assert key in launch

def test_date_utc():
    result = launches_2020()
    for launch in result["docs"]:
        dt = datetime.fromisoformat(launch["date_utc"].replace("Z", "+00:00"))
        assert dt.year == 2020

def test_success_launches():
    result = launches_2020()
    for launch in result["docs"]:
        assert launch["success"] in (True, False, None)




