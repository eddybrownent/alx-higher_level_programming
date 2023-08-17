#!/usr/bin/python3

"""
This script lists the State object with the name passed as argument
from the database
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
    state_name = sys.argv[4]

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
    Query the State object by name
    """
    state = session.query(State).filter_by(name=state_name).first()

    """
    Displaying the results
    """
    if state is not None:
        print(state.id)
    else:
        print("Not found")
