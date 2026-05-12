from pydantic import BaseModel

class BookCreateRequest(BaseModel):
    title: str
    author: str