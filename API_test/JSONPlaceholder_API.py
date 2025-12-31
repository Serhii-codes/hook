import requests
import pytest

# Task: Testing JSONPlaceholder API (fake posts)
#
# Endpoint: https://jsonplaceholder.typicode.com/posts
#
# Requirements:
# Send a POST request with JSON body:
# {
#   "title": "pytest demo",
#   "body": "learning API testing with POST",
#   "userId": 1
# }
# Verify:
# status code is 201
# response contains keys: id, title, body, userId
# title and body in the response match the request
# userId is an integer
# id is an integer and greater than 0


ENDPOINT = "https://jsonplaceholder.typicode.com/posts"

def fake_post():
    payload = {
        "title": "pytest demo",
        "body": "learning API testing with POST",
        "userId": 1
    }
    response = requests.post(ENDPOINT, json=payload)
    data = response.json()
    return data

def test_fake_code():
    response = requests.post(ENDPOINT)
    assert response.status_code == 201

def test_keys_id():
    data = fake_post()
    assert isinstance(data["id"], int)
    assert data["id"] > 0
    assert "id" in data

def test_keys_title():
    data = fake_post()
    assert "title" in data

def test_keys_body(fake_data):  # тут заюзав фікстуру
    assert "body" in fake_data

def test_keys_userid():
    data = fake_post()
    assert isinstance(data["userId"], int)
    assert "userId" in data

def test_match():
    data = fake_post()
    payload = {
        "title": "pytest demo",
        "body": "learning API testing with POST",
        "userId": 1
    }
    assert data["body"] == payload["body"]
    assert data["title"] == payload["title"]
    assert data["userId"] == payload["userId"]

def test_kayes():
    result = fake_post()
    assert set(result.keys()) >= {"id", "title", "body", "userId"}

