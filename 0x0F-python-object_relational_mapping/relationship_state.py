#!/usr/bin/python3
"""
This script defines a State model using SQLAlchemy ORM
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Represents a state entity in a MySQL database
    Attributes:
        __tablename__ (str): name of the MySQL table storing State records.
        id (sqlalchemy.Integer): The unique identifier of the state.
        name (sqlalchemy.String): name of the state.
        cities (sqlalchemy.orm.relationship): A relationship to associated City
    """

    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    # relationship between State and City
    cities = relationship("City", backref="state", cascade="all, delete")
