from src.core.entities.book import Book


class BookCreator:
    @staticmethod
    def create(title: str, author: str) -> Book:
        return Book(title=title, author=author)