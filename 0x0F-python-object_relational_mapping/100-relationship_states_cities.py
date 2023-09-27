#!/usr/bin/python3
"""
This script adds a City object to the
database with a relationship to a State object
"""

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access to the database and get the cities
    from the database.
    """

    # Constructing the MySQL database URL
    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3])

    # Creating an SQLALchemy engine and session
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Creating a State object and a City object
    cali_state = State(name='California')
    sanfra_city = City(name='San Francisco')

    # Establishing a relationship between City and State
    cali_state.cities.append(sanfra_city)

    # Adding the State object to the session and committing changes
    session.add(cali_state)
    session.commit()
