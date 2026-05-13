from lesson1_get_post_restapi.src.core.interfaces.book_repository import IBookRepository


class CreateBookUseCase:
    def __init__(self, repository: IBookRepository):
        self._repository = repository

    def execute(self, title: str, author: str):
        from lesson1_get_post_restapi.src.core.entities.book import Book
        new_book = Book(title=title, author=author)
        self._repository.save(new_book)
        return new_book
