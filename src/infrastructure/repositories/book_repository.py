from typing import List

from src.core.entities.book import Book
from src.core.interfaces.book_repository import IBookRepository


class BookRepository(IBookRepository):
    def __init__(self):
        self._books: List[Book] = []

    def save(self, book: Book):
        self._books.append(book)


    def get_all(self) -> List[Book]:
        return self._books


book_storage = BookRepository()