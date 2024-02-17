from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship

from .base import BaseModel


class Attachment(BaseModel):
    __tablename__ = 'attachments'

    original = Column(String, nullable=False)
    thumbnail = Column(String, nullable=False)

    businesses = relationship('Business', back_populates='logo')
    merchants = relationship('Merchant', back_populates='logo')

    def __str__(self):
        return f'{self.id}: {self.original}'
