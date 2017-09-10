from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .Entity import Entity

'''
Represents a pet.
'''
class Pet(Entity):
    __tablename__ = 'pet'

    birthDate = Column(Date)
    name = Column(String(50))
    type = Column(String(50))

    client = relationship('Client', back_populates = 'pets')
    clientID = Column(Integer, ForeignKey('client.id'))
