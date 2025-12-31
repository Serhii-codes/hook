import requests
import pytest
# Задача (нагадування):
# Тестуємо https://rickandmortyapi.com/api/character — потрібно перевірити:
# статус код = 200
# поле "results" — список і він не порожній
# кожен персонаж має ключі: "id", "name", "status"
# "status" ∈ {"Alive", "Dead", "unknown"}

URL = "https://rickandmortyapi.com/api/character"

def rick_and_morty():
    response = requests.get(URL)
    data = response.json()
    if response.status_code != 200:
        raise TypeError("API is failed")
    return data

def test_code():
    response = requests.get(URL)
    assert response.status_code == 200

def test_results():
    data = rick_and_morty()
    assert isinstance(data["results"], list)
    assert len(data["results"]) > 0

def test_charakter(rick_morty):
    for charakter in rick_morty["results"]:
        for key in ["id", "name", "status"]:
            assert key in charakter

def test_status_charakter(rick_morty):
    for status in rick_morty["results"]:
        assert status["status"] in ["Alive", "Dead", "unknown"], f'Unexpected status:{status["status"]}'




