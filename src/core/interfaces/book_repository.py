from abc import ABC, abstractmethod
from typing import List

from src.core.entities.book import Book


class IBookRepository(ABC):
    @abstractmethod
    def save(self, book: Book):
        pass

    @abstractmethod
    def get_all(self) -> List[Book]:
        pass