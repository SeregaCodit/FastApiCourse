from pydantic import BaseModel, Field, EmailStr, ConfigDict


class UserSchema(BaseModel):
    email: EmailStr
    bio: str | None = Field(max_length=100)


class UserAgeSchema(UserSchema):
    age: int = Field(ge=0, le=130)


class ForbiddenUserSchema(UserSchema):
    """This schema will raise an error if we try to create an instance with extra fields"""
    model_config = ConfigDict(extra="forbid")