
# Задача:
# У тебе є бот, який реагує на команду /hello і повертає "Hello, {username}!".
# Твоє завдання:
# Створити функцію handle_hello(username: str) -> str, яка повертає правильний текст.
# Написати тест з pytest, який перевіряє:
# Що функція повертає "Hello, John!" при введенні "John".
# Що якщо ім’я пусте — функція піднімає ValueError (використати pytest.raises).

import pytest

def handle_hello(username: str) -> str:
    if len(username) == 0:
        raise ValueError("The username is empty")
    return f"Hello, {username}!"

def test_handle():
    text = handle_hello("John")
    assert text == "Hello, John!"

def test_empty_user():
    with pytest.raises(ValueError, match="The username is empty"):
        handle_hello("")
