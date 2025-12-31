import requests
import pytest
# ТУТ ПРОБЛЕМА БУДА З ДОКУМЕНТАЦІЄЮ
# Task: Testing a Weather API Client
# You need to implement and tests a small Python function that works with a Weather API.
# Send a GET request to a public API endpoint:
# https://api.openweathermap.org/data/2.5/weather?q=Presov,SK&appid=e46acf3354c50c0af61b9662ce44281a&units=metric&lang=ua
# https://api.openweathermap.org/data/2.5/weather?q=UnknownCity,SK&appid=e46acf3354c50c0af61b9662ce44281a&units=metric&lang=ua - 404
# https://api.openweathermap.org/data/2.5/weather?q=Rio,SK&appid=INVALIDKEY&units=metric&lang=ua - 401
# Send a GET request to a public API endpoint:
# ✅ Valid city (e.g., Presov,SK) with a valid key → should return JSON with temperature.
# ❌ Invalid city (e.g., UnknownCity,SK) → should return 404.
# ❌ Invalid API key (e.g., INVALIDKEY) → should return error (401).
# Handle different cases:
# ✅ If the API returns 200 OK, extract the field "main.temp" from the JSON and return it as an integer.
# ❌ If the API returns 404, raise ValueError("City not found").
# ❌ If the API returns 401 (invalid key), raise PermissionError("Invalid API key").
# ❌ If the API returns any other error code (e.g., 500), raise RuntimeError("API error").
# ❌ If the "main.temp" field is missing in the JSON, raise KeyError("Temperature not available") - we always have this.


GOODWEATHER = 'https://api.openweathermap.org/data/2.5/weather?q=Presov,SK&appid=e46acf3354c50c0af61b9662ce44281a&units=metric&lang=ua'
NOCITY = 'https://api.openweathermap.org/data/2.5/weather?q=UnknownCity,SK&appid=e46acf3354c50c0af61b9662ce44281a&units=metric&lang=ua'
BADWEATHER = 'https://api.openweathermap.org/data/2.5/weather?q=Rio,SK&appid=INVALIDKEY&units=metric&lang=ua'

def get_temperature():
    response = requests.get(GOODWEATHER)
    data = response.json()
    if response.status_code != 200:
        raise ValueError("Unknown City")
    return data['main']['temp']

def get_city():
    response = requests.get(NOCITY)
    data = response.json()
    if response.status_code != 200:
        raise ValueError("City not found")
    return data

def get_api_status():
    response = requests.get(BADWEATHER)
    data = response.json()
    if response.status_code != 200:
        raise PermissionError("Invalid API key")
    return data

def get_temp():
    response = requests.get(GOODWEATHER)
    data = response.json()
    if 'main' not in data:                 #we always have this in json
        raise KeyError("Temperature not available")
    return data


def test_check_temp():
    response = requests.get(GOODWEATHER)
    assert response.status_code == 200

def test_get_temp():
    data = get_temperature()
    assert isinstance(data, float)

def test_get_city():
    response = requests.get(NOCITY)
    assert response.status_code == 404

def test_no_city_err():
    with pytest.raises(ValueError, match="City not found"):
        get_city()

def test_api_key():
    response = requests.get(BADWEATHER)
    assert response.status_code == 401

def test_api():
    with pytest.raises(PermissionError, match="Invalid API key"):
        get_api_status()

def test_other_err():
    with pytest.raises(RuntimeError, match="API error"):
        get_temperature()             #will be pass if we have problems with server, now in is not give us 500 error

def test_main_temp():
    with pytest.raises(KeyError, match="Temperature not available"):
        get_temp()                   #will be pass if we do not have 'main' in json, now we always have this in json

