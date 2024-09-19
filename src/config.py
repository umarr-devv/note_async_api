from pydantic_settings import BaseSettings
from yaml import safe_load
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


class Config(BaseSettings):
    database: str
    host: str
    user: str
    password: str
    jwt_private_key: str
    jwt_public_key: str


def create_config(config_file: str) -> Config:
    with open(BASE_DIR + '/' + config_file, mode='r', encoding='utf-8') as file:
        data = safe_load(file)
    return Config(**data)


config = create_config('config.yml')
