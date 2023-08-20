#!/usr/bin/python3
"""
This script changes the name of a State from the
database
"""

import sys
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Updates a State on the database
    """

    # Constructing the MySQL database URL
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(username,
                                                              password,
                                                              db_name)

    # Creating an SQLALchemy engine and session
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the State with ID 2
    state = session.query(State).filter(State.id == 2).first()
    state.name = "New Mexico"
    session.commit()    # Saves the changes to the database
