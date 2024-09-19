from datetime import datetime

from sqlalchemy import String, Text, ForeignKey, Integer, Column, Date, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base


class User(Base):
    __tablename__ = 'users'

    user_id: int = Column(Integer, primary_key=True, autoincrement=True)
    tg_id: int = Column(Integer, unique=True, nullable=True)
    created_on = Column(Date, default=datetime.now)
    update_on = Column(Date, default=datetime.now, onupdate=datetime.now)
    posts: list['Post'] = relationship(back_populates='user')

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.user_id})"

    def __repr__(self):
        return self.__str__()


class Post(Base):
    __tablename__ = 'posts'

    post_id: int = Column(Integer, primary_key=True, autoincrement=True)
    title: str = Column(String(length=64), unique=True)
    content: str = Column(Text, default='', server_default='')
    tags: Mapped[int] = Column(JSON)
    created_on: datetime = Column(Date, default=datetime.now)
    update_on: datetime = Column(Date, default=datetime.now, onupdate=datetime.now)
    user: User = relationship(back_populates='posts')
    user_id: int = mapped_column(ForeignKey('users.user_id'))
