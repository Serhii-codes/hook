# Task 1: GET request — RandomFOX API
# API description:
# RandomFox returns a random image of a fox via GET request — no authentication necessary.
# Example endpoint: GET https://randomfox.ca/floof/
# Requirements:
# Send a GET request to the endpoint.
# Verify:
# Status code is 200.
# Response is valid JSON.
# JSON contains a key "image" (string URL) and optionally "link".
# "image" must start with "https://" and end with a recognized image file extension (e.g., .jpg, .png, .gif).
# Negative tests:
# If you accidentally target a wrong endpoint (.../floofs/), assert that status code is 404.

import requests
import pytest

ENDPOINT = 'https://randomfox.ca/floof/'
ENDPOINT_ERR = 'https://randomfox.ca/floofs/'

response = requests.get(ENDPOINT)
data = response.json()

def get_fox_image():
    if response.status_code != 200:
        raise TypeError('API failer request')
    return data

def test_code_status():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200

def test_err_status():
    response = requests.get(ENDPOINT_ERR)
    assert response.status_code == 404

def test_key_image():
    result = get_fox_image()
    assert isinstance(result['image'], str)

def test_image_link():
    data = get_fox_image()
    assert 'image' in data
    assert 'link' in data


def test_link():
    result = get_fox_image()
    assert result['image'].startswith("https://")
    assert result['image'].endswith(('.jpg', '.png', '.gif'))





