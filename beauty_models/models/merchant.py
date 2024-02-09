from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from ..models import BaseModel


class Merchant(BaseModel):
    __tablename__ = 'merchants'

    sub = Column(String(200), unique=True, nullable=False)
    display_name = Column(String(100), nullable=False)
    phone_number = Column(String(100), nullable=True)

    logo_id = Column(Integer, ForeignKey('attachments.id'))
    business_id = Column(Integer, ForeignKey('businesses.id'))

    logo = relationship('Attachment', back_populates='merchants')
    businesses = relationship('Business', back_populates='owner')
