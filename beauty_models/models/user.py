from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship

from .base import BaseModel


class User(BaseModel):
    __tablename__ = 'users'

    sub = Column(String(200), unique=True, nullable=False)
    display_name = Column(String(200), nullable=False)
    phone_number = Column(String(100), nullable=True)
    email = Column(String(100), nullable=True)

    businesses = relationship('Business', back_populates='owner')
