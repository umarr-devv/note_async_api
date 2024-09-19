import pydantic


class UserSchema(pydantic.BaseModel):
    username: str


class CreateUserSchema(UserSchema):
    password: str


class GetUserSchema(UserSchema):
    user_id: int
    create_on: str
    update_on: str
