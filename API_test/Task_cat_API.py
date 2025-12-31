import pytest
import requests

# Check that the returned value is a dictionary.
# Check that the dictionary has keys "fact" and "length".
# Check that "fact" is a non-empty string.
# Check that "length" is an integer and matches the length of the "fact" string.
# Write a tests to verify that if the API returns a status code other than 200, the function raises a TypeError.
# (Hint: You can simulate this by temporarily changing the API URL to an invalid one inside the tests.)


CATE_FACT = "https://catfact.ninja/fact"

def get_random_fact():
    response = requests.get(CATE_FACT)
    data = response.json()
    if response.status_code != 200:
        raise TypeError("API request failed")
    return {"fact": data["fact"], "length": data["length"]}

def test_returned_value():
    result = get_random_fact()
    assert isinstance(result, dict)

def test_checking_value():
    result = get_random_fact()
    assert "fact" in result
    assert "length" in result

def test_type_value():
    result = get_random_fact()
    assert isinstance(result["fact"], str)
    assert result["length"] == len(result["fact"])
    assert len(result["fact"]) > 0
    assert isinstance(result["length"], int)


def test_response():
    with pytest.raises(TypeError, match="API request failed"):
        get_random_fact()   #тут треба зломати API лінк щоб пройшов тест















