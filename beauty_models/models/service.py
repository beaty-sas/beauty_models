from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from .base import BaseModel


class Service(BaseModel):
    __tablename__ = 'services'

    name = Column(String(200), unique=True, nullable=False)

    logo_id = Column(Integer, ForeignKey('attachments.id'))

    logo = relationship('Attachment', back_populates='services')
    business = relationship('Business', secondary='business_services_association', back_populates='services')
