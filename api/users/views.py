import fastapi
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.users.schemas import CreateUserSchema, GetUserSchema
from src.database import db_tools
from api.users.crud import create_user

router = fastapi.APIRouter(prefix='/user', tags=['users'])


@router.post('/create',
             response_model=GetUserSchema,
             status_code=fastapi.status.HTTP_201_CREATED)
async def on_create_user(user_in: CreateUserSchema,
                         session: AsyncSession = Depends(db_tools.session_dependency)):
    user = await create_user(session, user_in)
    return GetUserSchema(
        user_id=user.user_id,
        username=user.username,
        create_on=str(user.created_on),
        update_on=str(user.update_on)
    )
