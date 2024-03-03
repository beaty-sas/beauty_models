from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship

from .base import BaseModel


class Attachment(BaseModel):
    __tablename__ = 'attachments'

    original = Column(String, nullable=False)
    thumbnail = Column(String, nullable=False)

    businesses_logo = relationship('Business', back_populates='logo')
    businesses_banner = relationship('Business', back_populates='banner')
    merchants = relationship('Merchant', back_populates='logo')
    bookings = relationship('Booking', back_populates='attachments', secondary='booking_attachments_association')

    def __str__(self):
        return f'{self.id}: {self.original}'
