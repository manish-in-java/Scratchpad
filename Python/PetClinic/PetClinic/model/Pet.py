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

    '''
    Serializes this entity as JSON.
    '''
    def serialize(self):
        return {
                "birthDate" : self.birthDate
                , "client" : self.client.firstName + self.client.lastName
                , "name" : self.name
                , "type" : self.type
            }
