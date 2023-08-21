#!/usr/bin/python3
"""
This script displays Cities along with the States
they contain in a database
"""

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_base = sys.argv[3]

    # Connect to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(username, password, db_base,))

    # Create necessary tables in the database
    Base.metadata.create_all(engine)

    # Start a session to communicate with the databse
    Session = sessionmaker(bind=engine)
    session = Session()

    # gets and displays State-city info
    state_city = session.query(State).join(City).order_by(City.id).all()

    for state in state_city:
        for city in state.cities:
            print("{}: {} -> {}".format(city.id, city.name, state.name))
