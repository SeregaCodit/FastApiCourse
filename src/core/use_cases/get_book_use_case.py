from typing import List

from src.core.entities.book import Book
from src.core.interfaces.book_repository import IBookRepository


class GetAllBooksUseCase:
    def __init__(self, repository: IBookRepository):
        self._repository = repository

    def execute(self) -> List[Book]:
        return self._repository.get_all()