import pytest
# Task 1: Library System (OOP)
# Description:
# Create a simple library system with the following requirements:
# A Book class that has:
# title (str)
# author (str)
# year (int)
# A Library class that can:
# add_book(book) — adds a Book instance
# remove_book(title) — removes a book by its title (raises ValueError if not found)
# find_books_by_author(author) — returns a list of books by the given author
# get_all_books() — returns all books in the library
# Tests to write:
# Test adding and removing books
# Test searching by author
# Test error when removing a non-existing book
# Use fixture for initial book collection

class Book:
    def __init__(self, title: str, author: str, year: str):
        self.title = title
        self.author = author
        self.year = year
    def __str__(self):
        return f'{self.title}, by {self.author}, published in {self.year}'
class Library:
    def __init__(self):
        self.book = []
    def add_book(self, book):
        self.book.append(book)
    def remove_book(self, title):
        for book in self.book:
            if book.title == title:
                self.book.remove(book)
                return
        raise ValueError('Title not found')
    def find_book_by_author(self, author):
        return [book for book in self.book if book.author == author]
    def get_all_books(self):
        return self.book

def test_add_book(books_in_shelf):
    books = books_in_shelf.get_all_books()
    assert len(books) == 2
    assert any(book.title == '1984' for book in books)

def test_remove_book(books_in_shelf):
    books = books_in_shelf.get_all_books()
    assert len(books) == 2

def test_notexist_book():
    library = Library()
    book = Book('Freedom', 'Shevchenko T.G', '1897')
    library.add_book(book)
    with pytest.raises(ValueError, match='Title not found'):
        library.remove_book('Live in UA')
    assert library.get_all_books() == [book]

def test_find_author(check_books_in_shelf):
    books = check_books_in_shelf.get_all_books()
    assert books[0].author == 'Shevchenko T.G'
