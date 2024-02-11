from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import DECIMAL
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from .base import BaseModel


class Offer(BaseModel):
    __tablename__ = 'offers'

    name = Column(String(200), unique=True, nullable=False)
    price = Column(DECIMAL(precision=10, scale=2), nullable=False)  # type: ignore
    duration = Column(Integer, nullable=False)

    businesses = relationship('Business', secondary='business_offers', back_populates='offers')
    booking = relationship('Booking', secondary='booking_offers_association', back_populates='offers')
