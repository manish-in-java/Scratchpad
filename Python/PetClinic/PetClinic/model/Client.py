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

    '''
    Serializes this entity as JSON.
    '''
    def serialize(self):
        return {
                "building" : self.building
                , "country" : self.country
                , "district" : self.district
                , "firstName" : self.firstName
                , "lastName" : self.lastName
                , "locality" : self.locality
                , "postCode" : self.postCode
                , "street" : self.street
                , "town" : self.town
                , "pets" : [pet.serialize() for pet in pets]
            }
