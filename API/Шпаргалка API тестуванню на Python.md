1. **HTTP-запити (requests)**
```python
import requests

# GET
response = requests.get("https://api.example.com/posts")
response.status_code        # HTTP статус
response.json()             # Парсить JSON
response.text               # Текст відповіді

# POST
payload = {"title": "Test", "body": "Hello"}
response = requests.post("https://api.example.com/posts", json=payload)

# PUT / PATCH
update = {"title": "Updated"}
response = requests.put("https://api.example.com/posts/1", json=update)

# DELETE
response = requests.delete("https://api.example.com/posts/1")


```
**Підказка:** Завжди перевірти **status_code** + **структуру JSON**.

2. Типові асерти в pytest
```python

def test_get_posts():
    response = requests.get("https://api.example.com/posts")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert "title" in data[0]

```
- `assert response.status_code == 200` — перевірка успішності.
- `assert "key" in data` — перевірка наявності ключа в JSON.
- `assert data[0]["id"] == 1` — перевірка конкретного значення.

3. **Негативні кейси**
- Невірний endpoint → очікуємо 404
- Відсутні поля в POST → 400
- Неавторизований доступ → 401 / 403
```python

def test_invalid_endpoint():
    response = requests.get("https://api.example.com/wrong")
    assert response.status_code == 404
```

4. **Фікстури в pytest для API**
```python
import pytest

@pytest.fixture
def base_url():
    return "https://api.example.com"

@pytest.fixture
def auth_headers():
    return {"Authorization": "Bearer my_token"}

def test_get_posts(base_url, auth_headers):
    response = requests.get(f"{base_url}/posts", headers=auth_headers)
    assert response.status_code == 200
    
```
**Плюс фікстур:** зручно централізувати URL, токени, заголовки.

5. [**Параметризація тестів**](obsidian://open?vault=Obsidian%20Vault&file=Python%2FPytest%2FParametrize)
```python

@pytest.mark.parametrize("post_id, expected_title", [
    (1, "Hello World"),
    (2, "Python Tips")
])
def test_post_titles(base_url, post_id, expected_title):
    response = requests.get(f"{base_url}/posts/{post_id}")
    assert response.status_code == 200
    assert response.json()["title"] == expected_title
```
Дуже зручно для перевірки кількох ендпоінтів одним тестом.

 **6. Практичні поради**
1. JSON Schema — перевіряй формат відповіді.
2. Використовуй timeout у `requests`:
```python
response = requests.get(url, timeout=5)
```
3. Логи:
    - `print(response.json())` — під час розробки.
    - Для pytest можна підключати `caplog` або `logging`.
4. Використовуй `pytest.raises` для перевірки виключень при неправильних даних.

#sh3 #pytest #api