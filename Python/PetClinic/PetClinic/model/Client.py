from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from .Person import Person
from .Pet import Pet

'''
Represents a client.
'''
class Client(Person):
    __tablename__ = 'client'

    building = Column(String(50))
    country = Column(String(50))
    district = Column(String(50))
    locality = Column(String(50))
    postCode = Column(String(50))
    province = Column(String(50))
    street = Column(String(50))
    town = Column(String(50))

    pets = relationship('Pet', back_populates = 'client', order_by = Pet.name)
