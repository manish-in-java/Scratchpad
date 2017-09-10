from sqlalchemy import Column, String

from .Entity import Entity

'''
Represents a person.
'''
class Person(Entity):
    __abstract__ = True

    firstName = Column(String(50))
    lastName = Column(String(50))
