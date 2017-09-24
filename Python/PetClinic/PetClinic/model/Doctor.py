from sqlalchemy import Column, String

from .Person import Person

class Doctor(Person):
    """
    Represents a doctor at the pet clinic.

    Extends:
        Person
    """
    __tablename__ = 'doctor'
