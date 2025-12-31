import requests
import pytest
# Задача:
# Є API, яке повертає інформацію про погоду. Ендпоінт:
# GET https://api.open-meteo.com/v1/forecast?latitude=50.45&longitude=30.52&current_weather=true
# Твоє завдання:
# Написати тест, який:
# Перевіряє, що відповідь має статус 200.
# Перевіряє, що поле current_weather є у відповіді.
# Перевіряє, що значення temperature — число.
# Використовуй pytest та бібліотеку requests.
# Не забувай, що тест має падати, якщо API змінить структуру.

WEATHER = "https://api.open-meteo.com/v1/forecast?latitude=50.45&longitude=30.52&current_weather=truer"

def get_weather():
    response = requests.get(WEATHER)
    data = response.json()
    if response.status_code != 200:
        raise TypeError("API request failed")
    return data

def test_response():
    response = requests.get(WEATHER)
    assert response.status_code == 200


def test_get_temperature():
    result = get_weather()
    assert "current_weather" in result
    assert isinstance(result["current_weather"]["temperature"], (int, float))


def test_get_weather():
    with pytest.raises(TypeError, match="API request failed"):
        get_weather()

def test_temperature_city():                  #переверіка тепп.для міста
    result = get_weather()
    temp = result["current_weather"]["temperature"]
    assert isinstance(temp, (int, float)),  f" The temperature type is {type(temp)}" #пояснення
    assert -20 <= temp <= 40, f" The temperature is out of range {temp}"