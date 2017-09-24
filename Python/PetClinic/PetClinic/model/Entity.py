from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

Base = declarative_base()
Engine = create_engine('sqlite:///:memory:', echo = False)
Session = Session(Engine)

class Entity(Base):
    """
    Represents a domain entity.

    Attributes:
        id  The unique identifier of the entity instance.
    """
    __abstract__ = True

    id = Column(Integer, primary_key = True)

    @classmethod
    def count(clazz, *criteria):
        """
        Finds the number of entities matching specified criteria.

        Params:
            criteria    A sequence of criteria to use for finding the
                        required entities. If no criteria are specified,
                        the count of all entities of this type is returned.
        Returns:
            The number of entities matching the specified criteria.
        """
        if (criteria is not None and len(criteria) > 0):
            # Find the number of entities matching the specified criteria.
            return clazz.__query().filter(*criteria).count()
        else:
            # Find the number of all entities.
            return clazz.__query().count()

    def delete(self):
        """
        Deletes this entity instance.
        """
        Session.delete(self)
        Session.flush

    @classmethod
    def find(clazz, *criteria):
        """
        Finds all entity instances matching specified criteria.

        Params:
            criteria    A sequence of criteria to use for finding the
                        required entities. If no criteria are specified,
                        all entities of this type is returned.
        Returns:
            The entities matching the specified criteria.
        """
        return clazz.__query().filter(*criteria).all()

    @classmethod
    def findAll(clazz, *order):
        """
        Finds all entity instances of this type.

        Params:
            order   Optional criteria to apply for sorting the entities.
        Returns:
            All entities of this type, sorted by the specified criteria, if
            specified.
        """
        return clazz.__query().order_by(*order).all()

    @classmethod
    def findOne(clazz, id):
        """
        Finds an entity instance matching a specified primary key.

        Params:
            id   The unique identifier of the entity instance to find.
        Returns:
            The entity instance with the specified identifier, if found,
            None otherwise.
        """
        return clazz.__query().get(id)

    @classmethod
    def page(clazz, page, records, *order):
        """
        Finds a single page of entity instances.

        Params:
            page    The page number to find.
            records The number of records in the page to find.
            order   Optional criteria to apply for sorting the entities.
        Returns:
            The specified page of entities, if found.
        """
        return clazz.__query().order_by(*order).limit(records).offset((page - 1) * records).all()

    def save(self):
        """
        Saves this entity instance.

        Returns:
            The saved entity instance.
        """
        Session.add(self)
        Session.flush

        return self

    @classmethod
    def __query(clazz):
        """
        Creates an ad-hoc query for the domain entity.

        Returns:
            A query that can be executed on the entity type.
        """
        return Session.query(clazz)
