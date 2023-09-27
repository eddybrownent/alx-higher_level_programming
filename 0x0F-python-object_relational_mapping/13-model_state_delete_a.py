#!/usr/bin/python3
"""
This script deletes all State with a name containing
the letter <a> from the database
"""

import sys
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Deletes a Stae on the database
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

    # Query the State objects whose name contains the letter 'a'
    states = session.query(State).filter(State.name.contains('a'))
    if states is not None:
        for state in states:
            session.delete(state)

    session.commit()
