import uvicorn

from contextlib import asynccontextmanager
from fastapi import FastAPI

from src.api.v1.book_router import router as book_router
from src.infrastructure.repositories.book_repository import book_storage
from src.core.entities.book import Book


# 1. Створюємо функцію lifespan
@asynccontextmanager
async def lifespan(app: FastAPI):
    # --- STARTUP: Логіка при запуску ---
    # Наповнюємо наше сховище початковими даними
    book_storage.save(Book(title="The Great Gatsby", author="F. Scott Fitzgerald"))
    book_storage.save(Book(title="To Kill a Mockingbird", author="Harper Lee"))

    print("Додаток запущено, дані завантажено в пам'ять.")

    yield  # Тут додаток працює і обробляє запити

    # --- SHUTDOWN: Логіка при зупинці ---
    # Тут можна закривати з'єднання з БД або чистити кеш
    print("Додаток зупиняється...")

app = FastAPI(
        title="Clean Architecture API",
        lifespan=lifespan
    )
app.include_router(book_router, prefix="/api/v1")

def main():

    uvicorn.run("main:app", reload=True)


if __name__ == "__main__":
    main()