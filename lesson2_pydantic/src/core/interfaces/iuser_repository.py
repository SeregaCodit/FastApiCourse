from abc import ABC, abstractmethod
from typing import List

from lesson2_pydantic.src.api.schemas.user_schema import UserSchema


class IUserRepository(ABC):
    @abstractmethod
    def add_user(self, user: UserSchema):
        pass


    @abstractmethod
    def get_users(self) -> List[UserSchema]:
        pass