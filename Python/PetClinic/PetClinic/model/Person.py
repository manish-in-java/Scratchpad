from sqlalchemy import Column, String

from .Entity import Entity

class Person(Entity):
    """
    Represents a person associated with the pet clinic.

    Extends:
        Entity
    Attributes:
        firstName   The first/given name for the person.
        lastName    The last/family/surname for the person.
    """
    __abstract__ = True

    firstName = Column(String(50))
    lastName = Column(String(50))

    def serialize(self):
        """
        Serializes this entity as JSON.
        """
        return {
                "id" : self.id
                , "firstName" : "" + self.firstName + ""
                , "lastName" : "" + self.lastName + ""
            }
