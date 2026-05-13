import uvicorn

from contextlib import asynccontextmanager
from fastapi import FastAPI

from lesson1_get_post_restapi.src.api.v1.book_router import router as book_router
from lesson1_get_post_restapi.src.infrastructure.repositories.book_repository import book_storage
from lesson1_get_post_restapi.src.core.entities.book import Book


@asynccontextmanager
async def lifespan(app: FastAPI):
    # --- STARTUP: launch logic ---
    # add books to storage
    book_storage.save(Book(title="The Great Gatsby", author="F. Scott Fitzgerald"))
    book_storage.save(Book(title="To Kill a Mockingbird", author="Harper Lee"))

    yield  # app works

    # --- SHUTDOWN: shutdown logic ---
    # close DB connection etc

app = FastAPI(
        title="Lesson1 API",
        lifespan=lifespan
    )
app.include_router(book_router, prefix="/api/v1")

def main():
    uvicorn.run("main:app", reload=True)


if __name__ == "__main__":
    main()