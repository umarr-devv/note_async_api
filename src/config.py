from pydantic_settings import BaseSettings


class Config(BaseSettings):
    database: str = 'fastapiproject'
    host: str = 'localhost'
    user: str = 'postgres'
    password: str = 'qal3ko8tFgzyuL3vBeQW55UFNN9KcLJfeRisBhugm3NYc0WoUIKbzThf8sn0SWKY'

    database_url: str = f"postgresql+asyncpg://{user}:{password}@{host}/{database}"
    database_echo: bool = True


config = Config()
