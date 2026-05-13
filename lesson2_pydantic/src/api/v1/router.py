from typing import List

from fastapi import APIRouter

from lesson2_pydantic.src.api.schemas.response_schemas import PostResponseSchema
from lesson2_pydantic.src.api.schemas.user_schema import UserSchema
from lesson2_pydantic.src.infrastructure.repositiries.list_user_repository import list_user_repository
from lesson2_pydantic.src.core.use_cases.create_user_usecase import CreateUserUseCase

users_router = APIRouter(prefix="/users", tags=["users"])


@users_router.post("/users",
             tags=["users"],
             summary="Create a new user",
             description="Create a new user with the given email, bio and age."
             )
def create_user(user: UserSchema) -> PostResponseSchema:
    try:
        create_user_use_case = CreateUserUseCase(list_user_repository)
        create_user_use_case.execute(user)
        response = PostResponseSchema(status=True, msg="User created successfully.")
    except Exception as e:
        response = PostResponseSchema(status=False, msg=str(e))
    return response


@users_router.get("/users",
                  tags=["users"],
                  summary="List all users",
                  description="List all users with the given email."
)
def get_all_users() -> List[UserSchema]:
    return list_user_repository.get_users()
