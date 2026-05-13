from pydantic import BaseModel, Field


class PostResponseSchema(BaseModel):
    status: bool
    msg: str