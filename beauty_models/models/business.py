from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Table
from sqlalchemy.orm import relationship

from . import Base
from .base import BaseModel

business_services = Table(
    'business_services_association',
    Base.metadata,
    Column('business_id', ForeignKey('businesses.id'), primary_key=True),
    Column('service_id', ForeignKey('services.id'), primary_key=True),
)


class Business(BaseModel):
    __tablename__ = 'businesses'

    name = Column(String(200), unique=True, nullable=False)
    display_name = Column(String(200), nullable=False)
    phone_number = Column(String(100), nullable=True)
    web_site = Column(String(100), nullable=True)

    owner_id = Column(Integer, ForeignKey('users.id'))
    location_id = Column(Integer, ForeignKey('locations.id'))

    owner = relationship('User', back_populates='businesses')
    location = relationship('location', back_populates='businesses')
    services = relationship('Service', secondary=business_services, back_populates='business')
