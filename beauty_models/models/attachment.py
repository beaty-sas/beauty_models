from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship

from .base import BaseModel


class Attachment(BaseModel):
    __tablename__ = 'attachments'

    original = Column(String, nullable=False)
    thumbnail = Column(String, nullable=False)

    services = relationship('Service', back_populates='logo')
