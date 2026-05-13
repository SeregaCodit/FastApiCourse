import uvicorn
from fastapi import FastAPI

from lesson2_pydantic.src.api.schemas.user_schema import UserSchema, UserAgeSchema, ForbiddenUserSchema
from lesson2_pydantic.src.api.v1.router import users_router
from lesson2_pydantic.src.infrastructure.repositiries.list_user_repository import UserRepository



data = {
    "email": "exemple@mail.com",
    "bio": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
    "age": 12
}

data_wo_age = {
    "email": "exemple@mail.com",
    "bio": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
    "extra_field": "this field is not defined in the schema"
}

user = UserSchema(**data)
print(repr(user))

user_age = UserAgeSchema(**data)
print(repr(user_age))

try:
    user_forbidden = ForbiddenUserSchema(**data_wo_age)
    print(repr(user_forbidden))
except Exception as e:
    print(repr(e))

app = FastAPI()
app.include_router(users_router, prefix="/api/v1")

def main():
    uvicorn.run("main:app", reload=True)



if __name__ == "__main__":
    main()