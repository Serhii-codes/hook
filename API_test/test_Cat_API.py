# Task 2: POST request — HTTP Cat API
# API description:
# HTTP Cat provides images of cats for each HTTP status code. It doesn't support POST requests.
# Example endpoint: GET https://http.cat/404
# Requirements:
# Attempt a POST request to the base URL or a status-specific endpoint.
# Verify:
# It fails—either with status code 405 (Method Not Allowed) or 404.
# Explicitly assert that POST is not supported and the status code is in the range for errors (>= 400).
# Additionally:
# Perform a GET to a known cat image endpoint (e.g., /404) and ensure the Content-Type header starts
# with image/ (verifies it's an image).

import requests
import pytest

URL = 'https://http.cat/404'

def test_post():
    response = requests.post(URL, json={'title': 'Cat in a bed'})
    assert response.status_code >= 400

def test_get_cat():
    response = requests.get(URL)
    assert response.status_code == 200
    assert response.headers['Content-Type'].startswith('image/')


