from datetime import datetime

from sqlalchemy import String, Text, ForeignKey, Integer, Column, Date, JSON, LargeBinary
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base


class User(Base):
    __tablename__ = 'users'

    user_id: int = Column(Integer, primary_key=True, autoincrement=True)
    username: str = Column(String, unique=True, nullable=False)
    tg_id: int = Column(Integer, unique=True, nullable=True)
    password: bytes = Column(LargeBinary, nullable=False)
    created_on = Column(Date, default=datetime.now)
    update_on = Column(Date, default=datetime.now, onupdate=datetime.now)
    posts: Mapped[list['Post']] = relationship(back_populates='user')

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.user_id})"

    def __repr__(self):
        return self.__str__()


class Post(Base):
    __tablename__ = 'posts'

    post_id: int = Column(Integer, primary_key=True, autoincrement=True)
    title: str = Column(String(length=64), unique=True)
    content: str = Column(Text, default='', server_default='')
    tags = Column(JSON)
    created_on: datetime = Column(Date, default=datetime.now)
    update_on: datetime = Column(Date, default=datetime.now, onupdate=datetime.now)
    user: Mapped['User'] = relationship(back_populates='posts')
    user_id: int = Column(ForeignKey('users.user_id'))

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.user_id})"

    def __repr__(self):
        return self.__str__()
