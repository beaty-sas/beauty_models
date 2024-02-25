from sqlalchemy import Column
from sqlalchemy import Date
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import Time
from sqlalchemy.orm import relationship

from ..models import BaseModel


class WorkingHours(BaseModel):
    __tablename__ = 'working_hours'

    date = Column(Date, nullable=False, index=True)
    opening_time = Column(Time, nullable=False)
    closing_time = Column(Time, nullable=False)

    business_id = Column(Integer, ForeignKey('businesses.id'), nullable=False)

    business = relationship('Business', back_populates='working_hours')

    def __str__(self):
        return f'{self.id}: {self.date} {self.opening_time} - {self.closing_time}. Business: {self.business_id}'
