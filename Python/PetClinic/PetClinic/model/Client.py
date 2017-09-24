from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from .Person import Person
from .Pet import Pet

class Client(Person):
    """
    Represents a client of the pet clinic.

    Extends:
        Person
    Attributes:
        building    The name/number of the building in which the client
                    resides.
        locality    The name of the locality where the client resides.
        postCode    The postal code of the locality where the client resides.
        province    The name of the province/state where the client resides.
        street      The name of the street on which the client resides.
        town        The name of the town/city/village where the client resides.
        pets        Pets owned by the client and brought to the pet clinic
                    for medical care.
    """
    __tablename__ = 'client'

    building = Column(String(50))
    locality = Column(String(50))
    postCode = Column(String(50))
    province = Column(String(50))
    street = Column(String(50))
    town = Column(String(50))

    pets = relationship('Pet', back_populates = 'client', order_by = Pet.name)

    def serialize(self):
        """
        Serializes this entity as JSON.
        """
        return {
                "id" : self.id
                , "building" : "" + self.building + ""
                , "firstName" : "" + self.firstName + ""
                , "lastName" : "" + self.lastName + ""
                , "locality" : "" + self.locality + ""
                , "postCode" : "" + self.postCode + ""
                , "province" : "" + self.province + ""
                , "street" : "" + self.street + ""
                , "town" : "" + self.town + ""
                , "pets" : [pet.serialize() for pet in self.pets]
            }
