from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func

from app.database.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    email = Column(String, unique=True, nullable=False)

    phone = Column(String, nullable=True)

    hashed_password = Column(String, nullable=False)

    department = Column(String, nullable=True)

    role = Column(String, nullable=False)

    created_by = Column(String, nullable=True)

    is_active = Column(Boolean, default=True)

    last_login = Column(DateTime, nullable=True)

    created_at = Column(DateTime, server_default=func.now())