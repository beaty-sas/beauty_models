from geoalchemy2 import Geometry
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship

from .base import BaseModel


class Location(BaseModel):
    __tablename__ = 'locations'

    name = Column(String, nullable=False)
    geom = Column(Geometry('POINT', srid=4326))

    businesses = relationship('Business', back_populates='location')
