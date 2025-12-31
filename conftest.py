import pytest

from parity import BankAccount
from pytest_practice.OOP_tests.OOP_test_tuskBook import Book, Library
from pytest_practice.Test_API.JSONPlaceholder_API import fake_post
from pytest_practice.Test_API.RickMortyAPI import rick_and_morty
from pytest_practice.Test_API.RickMorty2 import rick_morty_2
@pytest.fixture
def database():
    print('connection to database')
    data = 10
    yield data
    print('close connection')

@pytest.fixture
def ver_user_data():
    return {'username': "magula"}

@pytest.fixture
def space_cleaner():
    return {'input': '     Hello         '}

@pytest.fixture
def pass_check():
    check = {
        'good':'hdgrygu86',
        'short':'ytqh5',
        'long':'hfgdtripkhfndjtylghs783rbwsx722',
        'no_digit': 'udghftyepl',
        'wrong': 888
}
    return check

@pytest.fixture
def email_check():
    valid = {
        'correct':"room@get.com",
        'incorrect': "testtest",
        'wrong_type': 15576
}
    return valid

@pytest.fixture
def clean_text():
    cleaner = {
        'norm': 'nice',
        'space':'            ',
        'empty':'',
        'incorrect': 475
}
    return cleaner

@pytest.fixture
def balance_checker():
    return BankAccount()

@pytest.fixture
def get_info():
    return BankAccount(80)

@pytest.fixture
def books_in_shelf():
    library = Library()
    books = [
        Book('Freedom', 'Shevchenko T.G', '1897'),
        Book('Live in UA', 'Shevchenko T.G', '1787'),
]
    new_book = Book('1984', 'Orwell', '1949')
    for book in books:
        library.add_book(book)
    library.add_book(new_book)
    library.remove_book('Live in UA')
    return library

@pytest.fixture()
def check_books_in_shelf():
    library = Library()
    books = [
        Book('Freedom', 'Shevchenko T.G', '1897'),
        Book('Live in UA', 'Shevchenko T.G', '1787'),
        Book('1984', 'Orwell', '1949')
]
    for book in books:
        library.add_book(book)
    return library


@pytest.fixture
def greetings_check():
    greetings = {
        "normal": "hello",
        "caps": "HELLO",
        "incorrect": "highway",
        "correct": "hi",
        "caps_1": "HEY"
    }
    return greetings

@pytest.fixture
def fake_data():
    data = fake_post()
    return data

@pytest.fixture
def rick_morty():
    data = rick_and_morty()
    return data

@pytest.fixture
def rick_morty_data():
    data = rick_morty_2()
    return data



