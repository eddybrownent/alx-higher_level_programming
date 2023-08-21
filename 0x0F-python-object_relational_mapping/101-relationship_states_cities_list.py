#!/usr/bin/python3
"""
This script lists all State objects and their corresponding
City object in the databse
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
                           format(username, password, db_base))

    # Create necessary tables in the database
    Base.metadata.create_all(engine)

    # Start a session to communicate with the databse
    Session = sessionmaker(bind=engine)
    session = Session()

    # getting and printing State and City infomation
    state_city = session.query(State).outerjoin(City).order_by(State.id,
                                                               City.id).all()

    for state in state_city:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))
