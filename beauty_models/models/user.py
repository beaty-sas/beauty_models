from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship

from .base import BaseModel


class User(BaseModel):
    __tablename__ = 'users'

    sub = Column(String(200), unique=True)
    display_name = Column(String(200), nullable=False)
    phone_number = Column(String(100), nullable=False)

    bookings = relationship('Booking', back_populates='user')
