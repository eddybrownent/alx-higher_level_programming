#!/usr/bin/python3

"""
This script adds a State 'Lousiana'
to the databse
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Extracting MySQL credentials from the command-line arguments
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    """
    Defining the connection URL
    """
    connect_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            username, password, database)

    """
    Creating an SQLAlchemy engine and establish a connection
    """
    engine = create_engine(connect_url)

    """
    Creating a session to interact with the database
    """
    Session = sessionmaker(bind=engine)
    session = Session()

    """
    Create and add the new State object
    """
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    print(new_state.id)
