from sqlalchemy import Column, String

from .Person import Person

'''
Represents a doctor.
'''
class Doctor(Person):
    __tablename__ = 'doctor'
