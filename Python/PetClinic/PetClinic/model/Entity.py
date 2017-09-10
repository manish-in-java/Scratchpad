from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

Base = declarative_base()
Engine = create_engine('sqlite:///:memory:', echo = False)
Session = Session(Engine)

'''
Represents a domain entity.
'''
class Entity(Base):
    __abstract__ = True

    '''
    The unique primary key for the entity.
    '''
    id = Column(Integer, primary_key = True)

    '''
    Finds the number of entities matching specified criteria.
    '''
    @classmethod
    def count(clazz, *criteria):
        if (criteria is not None and len(criteria) > 0):
            # Find the number of entities matching the specified criteria.
            return clazz.query().filter(*criteria).count()
        else:
            # Find the number of all entities.
            return clazz.query().count()

    '''
    Deletes this entity instance.
    '''
    def delete(self):
        Session.delete(self)
        Session.flush

    '''
    Finds all entity instances matching specified criteria.
    '''
    @classmethod
    def find(clazz, *criteria):
        return clazz.query().filter(*criteria).all()

    '''
    Finds all entity instances.
    '''
    @classmethod
    def findAll(clazz, order):
        return clazz.query().order_by(order).all()

    '''
    Finds an entity instance matching a specified primary key.
    '''
    @classmethod
    def findOne(clazz, id):
        return clazz.query().get(id)

    '''
    Finds a single page of entity instances.
    '''
    @classmethod
    def page(clazz, page, records, order):
        return clazz.query().order_by(order).limit(records).offset((page - 1) * records).all()

    '''
    Creates an ad-hoc query for the domain entity.
    '''
    @classmethod
    def query(clazz):
        return Session.query(clazz)

    '''
    Saves this entity instance.
    '''
    def save(self):
        Session.add(self)
        Session.flush

        return self
