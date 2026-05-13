from lesson2_pydantic.src.api.schemas.user_schema import UserSchema
from lesson2_pydantic.src.core.interfaces.iuser_repository import IUserRepository


class CreateUserUseCase:
    def __init__(self, repo: IUserRepository):
        self.repo = repo

    def execute(self, user: UserSchema):
        self.repo.add_user(user)
        return user