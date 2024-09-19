import jwt
import bcrypt
from src.config import config


def encode_jwt(payload: dict, private_key: str = config.jwt_private_key,
               algorithm: str = 'RS256'):
    return jwt.encode(payload, key=private_key, algorithm=algorithm)


def decode_jwt(token: str, public_key: str = config.jwt_public_key,
               algorithm: str = 'RS256'):
    return jwt.decode(
        token, key=public_key, algorithms=[algorithm]
    )


def hash_password(password: str) -> bytes:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def is_valid_password(password: str, hashed_password: bytes) -> bool:
    return bcrypt.checkpw(password.encode(), hashed_password)
