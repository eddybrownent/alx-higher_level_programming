#!/usr/bin/python3
"""
This script fetches and prints all City objects from
the database
"""
import sys
from model_state import State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Fetch and print City objects from the database
    """

    # Constructing the MySQL database URL
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(username,
                                                              password,
                                                              db_name)
    # Creating an SQLAlchemy engine and session
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query and print City objects with their corresponding State names
    city_state_q = session.query(City, State).join(State).order_by(City.id)
    for city, state in city_state_q:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
