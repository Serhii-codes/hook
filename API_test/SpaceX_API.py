import requests
import pytest
from datetime import datetime, timezone
from dateutil.parser import parse
# API Testing Task — SpaceX Launch Data
# API Endpoint:
# https://api.spacexdata.com/v4/launches/latest
# (You don’t need authentication; it’s a public API.)
# Your Task:
# Send a GET request to the endpoint above.
# Verify that:
# The response status code is 200.
# The response contains a key "name" which is a string.
# The "date_utc" value can be parsed into a valid datetime object.
# The "success" field is either True, False, or None (because not all launches have a result yet).
# The "id" field is a non-empty string.


SPACEX = "https://api.spacexdata.com/v4/launches/latest"
NEXT = "https://api.spacexdata.com/v4/launches/next"


def get_space():
    response = requests.get(SPACEX)
    data = response.json()
    if response.status_code != 200:
        raise TypeError("API request failed")
    return data

def get_next():
    response_2 = requests.get(NEXT)
    data = response_2.json()
    if response_2.status_code != 200:
        raise TypeError("API request failed")
    else:
        return data


def test_response():
    response = requests.get(SPACEX)
    assert response.status_code == 200

def test_type_name():
    result = get_space()
    assert isinstance(result["name"], str) == True

def test_utc_value():
    result = get_space()
    utc_time = result["date_utc"]
    utc_time_datetime = parse(utc_time)
    assert isinstance(utc_time_datetime, datetime)
    assert result["date_utc"] is not None # можна не перевіряти


def test_success_field():
    result = get_space()
    assert result["success"] in (True, False, None)


def test_id_field():
    result = get_space()
    assert len(result["id"]) > 0

def test_time_next():
    result = get_next()
    next_time = result["date_utc"]
    next_datetime = parse(next_time)
    assert isinstance(next_datetime, datetime)
    # now = datetime.now(timezone.utc)              # Поточний час у UTC
    assert next_datetime.tzinfo is not None               # Стабільна перевірка — дата повинна бути offset-aware

def test_time_latest():
    result = get_space()
    latest_time = result["date_utc"]
    latest_datetime = parse(latest_time)
    assert isinstance(latest_datetime, datetime)
    assert latest_datetime.tzinfo is not None    # Стабільна перевірка — дата повинна бути offset-aware




