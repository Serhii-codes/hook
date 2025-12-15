- `with pytest.raises(ErrorType, match="...") as e:` — перевірка, що функція викидає помилку
- Приклади:
    - `ZeroDivisionError`
    - `ValueError`
    - `match="division by zero"` — перевірка тексту помилки
- `pytest --setup-show` — показує як працюють фікстури
response.raise_for_status() - бібліотека саме кидає момилку від API



#sh01 