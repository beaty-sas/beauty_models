from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import Table
from sqlalchemy.orm import relationship

from ..models import BaseModel

booking_services_association = Table(
    'booking_services_association',
    BaseModel.metadata,
    Column('booking_id', ForeignKey('bookings.id'), primary_key=True),
    Column('service_id', ForeignKey('services.id'), primary_key=True),
)


class Booking(BaseModel):
    __tablename__ = 'bookings'

    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)

    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    business_id = Column(Integer, ForeignKey('businesses.id'), nullable=False)

    user = relationship('User', back_populates='bookings')
    services = relationship('Service', secondary=booking_services_association, back_populates='bookings')
