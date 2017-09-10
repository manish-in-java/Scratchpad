from sqlalchemy import Column, String

from .Entity import Entity

'''
Represents a person.
'''
class Person(Entity):
    __abstract__ = True

    firstName = Column(String(50))
    lastName = Column(String(50))

    '''
    Serializes this entity as JSON.
    '''
    def serialize(self):
        return {
                "firstName" : self.firstName
                , "lastName" : self.lastName
            }
