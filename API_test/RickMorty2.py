import requests
import pytest

# Task: Testing the Rick and Morty API
# You need to write pytest tests for the public Rick and Morty API:
# https://rickandmortyapi.com/
# What to tests
# GET request to https://rickandmortyapi.com/api/character:
# Status code is 200.
# The field "results" is a list and it’s not empty.
# Every character has the keys: "id", "name", "status".
# "status" must be one of: {"Alive", "Dead", "unknown"}.
# Negative cases for GET request:
# Invalid endpoint should return 404.
# If you request a character that does not exist (e.g., /api/character/9999999), you should check the error response.
# POST request (this API is read-only, so POST will fail):
# If you try POST with some data, the API should not allow it and must return an error status (e.g., 405 Method Not Allowed).
# Write a tests that confirms the API rejects POST requests.


URL = "https://rickandmortyapi.com/api/character"
NEGATIVEURL = "https://rickandmortyapi.com/api1/character"
NEGATIVECHR = "https://rickandmortyapi.com/api/character999999"

def rick_morty_2():
    response = requests.get(URL)
    if response.status_code != 200:
        raise ValueError("API failed")
    data = response.json()
    return data

def test_code_200():
    response = requests.get(URL)
    assert response.status_code == 200

def test_type_results(rick_morty_data):
    assert "results" in rick_morty_data
    assert isinstance(rick_morty_data["results"], list)

def test_keys_chr(rick_morty_data):
    for character in rick_morty_data["results"]:
        for key in ["id", "name", "status"]:
            assert key in character

def test_status_chr(rick_morty_data):
    for key in rick_morty_data["results"]:
        assert key["status"] in ["Alive", "Dead", "unknown"],  f'Unexist status: {key["status"]}'

####Negative tests

def test_negative_chr():
    response = requests.get(NEGATIVECHR)
    assert response.status_code == 404

#### POST request

def test_post_chr():
    payload = {
        "results": [{"id": -8, "name": "Lesia Ukrainka", "status": "fly"}]
    }
    response = requests.post(URL, json=payload)
    assert response.status_code == 404

