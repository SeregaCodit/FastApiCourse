from typing import List

from lesson1_get_post_restapi.src.core.entities.book import Book
from lesson1_get_post_restapi.src.core.interfaces.book_repository import IBookRepository


class BookRepository(IBookRepository):
    def __init__(self):
        self._books: List[Book] = []

    def save(self, book: Book):
        self._books.append(book)


    def get_all(self) -> List[Book]:
        return self._books


book_storage = BookRepository()