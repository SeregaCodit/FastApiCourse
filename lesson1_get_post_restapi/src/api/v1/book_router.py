from typing import List

from fastapi import APIRouter, HTTPException

from lesson1_get_post_restapi.src.core.entities.book import Book
from lesson1_get_post_restapi.src.infrastructure.repositories.book_repository import book_storage
from lesson1_get_post_restapi.src.core.use_cases.create_book_use_case import CreateBookUseCase
from lesson1_get_post_restapi.src.core.use_cases.get_book_use_case import GetAllBooksUseCase
from lesson1_get_post_restapi.src.api.schemas.book_reuest import BookCreateRequest


router = APIRouter(prefix="/book", tags=["books"])

create_book_use_case = CreateBookUseCase(book_storage)
get_all_books_use_case = GetAllBooksUseCase(book_storage)


@router.post("/",
             tags=["books"],
             summary="Add a new book",
             description="Create a new book with the given title and author.",
             )
def create_book(request: BookCreateRequest) -> Book:
    return create_book_use_case.execute(request.title, request.author)


@router.get("/books",
            tags=["books"],
            summary="Get all books",
            description="Retrieve a list of all books in the system.",
            )
def get_all_books() -> List[Book]:
    return get_all_books_use_case.execute()


@router.get("/{book_id}",
            tags=["books"],
            summary="Get a book by ID",
            description="Retrieve a book by its unique ID."
            )
def get_book(book_id: int) -> Book:
    all_books = book_storage.get_all()

    for book in all_books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

