#!/usr/bin/python3
"""
This script defines a City class for
SQALchemy ORM
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class City(Base):
    """
    City class representing a city in the database
    Inherits from the Base class from model_state
    """

    __tablename__ = 'cities'

    # Columns definition
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
