from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from bloom.postgres import Base
from bloom.models.user import UserModel


class EventModel(Base):
    __tablename__ = "events"
    event_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    event_start = Column(DateTime, default=datetime.utcnow)
    event_end = Column(DateTime, default=datetime.utcnow)
    creator_id = Column(Integer, ForeignKey("users.id"))
    creator = relationship("UserModel")
