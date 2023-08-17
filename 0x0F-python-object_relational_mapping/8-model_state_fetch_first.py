#!/usr/bin/python3

"""
This script lists the first State objects from the database
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
    Query and display the first State object
    """
    state = session.query(State).order_by(State.id).first()

    if state is not None:
        print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")
