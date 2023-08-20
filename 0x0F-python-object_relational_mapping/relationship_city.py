#!/usr/bin/python3
"""
This script defines a City class to work with SQLAlchemy ORM
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base, State


class City(Base):
    """
    City class representing a city in the database

    Attributes:
        __tablename__ (str): table name of the class
        id (int): The unique identifier of the city
        name (str): name of the city
        state_id (int): foreign key referencing the associated state's ID
    """

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
