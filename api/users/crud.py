from sqlalchemy.ext.asyncio import AsyncSession

from api.users.schemas import CreateUserSchema
from src.models import User
from src.utils import hash_password


async def create_user(session: AsyncSession, user_in: CreateUserSchema) -> User:
    user = User(username=user_in.username,
                password=hash_password(user_in.password))
    session.add(user)
    await session.commit()
    return user
