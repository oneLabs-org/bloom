from sqlalchemy import Boolean, Column, Integer, String, DateTime, func, Enum
from datetime import datetime
from enum import StrEnum
from bloom.postgres import Base


class UserRole(StrEnum):
    author: str = "author"
    reviewer: str = "reviewer"
    admin: str = "admin"


class UserModel(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(100))
    last_name = Column(String(100))
    email = Column(String(255), unique=True, index=True)
    password = Column(String(100))
    role = Column(String(50), nullable=False, server_default=UserRole.author)
    is_verified = Column(Boolean, default=True)
    verified_at = Column(DateTime, nullable=True, default=None)
    registered_at = Column(DateTime, nullable=True, default=None)
    updated_at = Column(DateTime, nullable=True, default=None, onupdate=datetime.now)
    created_at = Column(DateTime, nullable=False, server_default=func.now())
