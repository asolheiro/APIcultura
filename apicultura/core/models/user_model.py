from sqlalchemy import String, Column
from sqlalchemy.orm import relationship
from apicultura.core.models.base import BModel


class User(BModel):
    __tablename__ = "users"

    username = Column(String(), unique=True)
    password = Column(String())
    email = Column(String(), unique=True)
    tasks = relationship("Task")
