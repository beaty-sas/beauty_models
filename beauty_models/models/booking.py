from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import DECIMAL
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import Table
from sqlalchemy.orm import relationship

from ..models import BaseModel

booking_offers_association = Table(
    'booking_offers_association',
    BaseModel.metadata,
    Column('booking_id', ForeignKey('bookings.id'), primary_key=True),
    Column('offer_id', ForeignKey('offers.id'), primary_key=True),
)


class Booking(BaseModel):
    __tablename__ = 'bookings'

    start_time = Column(DateTime(timezone=True), nullable=False)
    end_time = Column(DateTime(timezone=True), nullable=False)
    price = Column(DECIMAL, nullable=False)

    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    business_id = Column(Integer, ForeignKey('businesses.id'), nullable=False)

    user = relationship('User', back_populates='bookings')
    offers = relationship('Offer', back_populates='booking', secondary=booking_offers_association)
    business = relationship('Business', back_populates='bookings')
