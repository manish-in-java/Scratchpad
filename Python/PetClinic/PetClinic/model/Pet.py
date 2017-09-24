from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .Entity import Entity

class Pet(Entity):
    """
    Represents a pet that has been brought to the pet clinic at least once.

    Extends:
        Entity
    Attributes:
        birthDate   The date of birth for the pet.
        name        The pet name.
        type        The type of pet.
    """
    __tablename__ = 'pet'

    birthDate = Column(Date)
    name = Column(String(50))
    type = Column(String(50))

    client = relationship('Client', back_populates = 'pets')
    __clientID = Column(Integer, ForeignKey('client.id'))

    def serialize(self):
        """
        Serializes this entity as JSON.
        """
        return {
                "id" : self.id
                , "birthDate" : self.birthDate.strftime("%Y-%m-%d")
                , "client" : "" + self.client.name + ""
                , "name" : "" + self.name + ""
                , "type" : "" + self.type + ""
            }
