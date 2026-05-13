from typing import List

from lesson2_pydantic.src.api.schemas.user_schema import UserSchema


class UserRepository:
    def __init__(self):
        self._users: List[UserSchema] = list()

    def add_user(self, user: UserSchema):
        self._users.append(user)


    def get_users(self) -> List[UserSchema]:
        return self._users

list_user_repository = UserRepository() # ak singleton