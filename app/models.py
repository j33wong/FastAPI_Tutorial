from typing import Text
from sqlalchemy.orm import relationship

from sqlalchemy.sql.schema import ForeignKey
from .database import Base
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text

class Post(Base):
    __tablename__ = "posts"
    # columns
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String(256), nullable=False)
    content = Column(String(512), nullable=False)
    published = Column(Boolean, server_default=text('True'), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('Now()'))
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    # return the class of user automatically
    owner = relationship("User")


class User(Base):
    __tablename__ = "users"
    # columns
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String(128), nullable=False, unique=True)
    password = Column(String(128), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('Now()'))
    phone_number =Column(String(10))

class Vote(Base):
    __tablename__ = "votes"
    # columns
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
    post_id = Column(Integer, ForeignKey("posts.id", ondelete="CASCADE"), primary_key=True)
