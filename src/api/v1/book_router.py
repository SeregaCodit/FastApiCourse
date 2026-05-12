from fastapi import APIRouter, HTTPException

from src.core.entities.book import Book
from src.infrastructure.repositories.book_repository import book_storage
from src.core.use_cases.create_book_use_case import CreateBookUseCase
from src.core.use_cases.get_book_use_case import GetAllBooksUseCase
from src.api.schemas.book_reuest import BookCreateRequest


router = APIRouter(prefix="/book", tags=["books"])

create_book_use_case = CreateBookUseCase(book_storage)
get_all_books_use_case = GetAllBooksUseCase(book_storage)

@router.post("/", tags=["books"])
def create_book(request: BookCreateRequest) -> Book:
    return create_book_use_case.execute(request.title, request.author)


@router.get("/{book_id}", tags=["books"])
def get_book(book_id: int) -> Book:
    all_books = book_storage.get_all()

    for book in all_books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

