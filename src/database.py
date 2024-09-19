from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

from src.config import Config, config


class Base(DeclarativeBase):
    __abstract__ = True


class DataBaseTools:

    def __init__(self, _config: Config):
        self.url = f"postgresql+asyncpg://{config.user}:{config.password}@{config.host}/{config.database}"
        self.engine = create_async_engine(
            url=self.url
        )
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False
        )


db_tools = DataBaseTools(config)
