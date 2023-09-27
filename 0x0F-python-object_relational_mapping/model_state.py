#!/usr/bin/python3

"""
Thi module contains the defination of the State class
and Base instance to work with SQLAlchemy
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

"""
Creating a base class for declarative models
"""
Base = declarative_base()


class State(Base):
    """
    Class representing a state in  a database

    Attributes:
        __tablename__ (str): The table name
        id (int): The primary key for the state record
        name (str): The name of the state
    """

    __tablename__ = "states"

    """
    Defining the columns and their data types for the states table
    """
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
