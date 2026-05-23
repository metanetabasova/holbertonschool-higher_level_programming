#!/usr/bin/python3
"""
Print all City objects from the database, ordered by City.id.

Output format:
<state name>: (<city id>) <city name>
"""
import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_city import City
from model_state import Base, State


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        username, password, dbname
    )
    engine = create_engine(url, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    results = (
        session.query(State.name, City.id, City.name)
        .join(City, City.state_id == State.id)
        .order_by(City.id)
        .all()
    )

    for state_name, city_id, city_name in results:
        print("{}: ({}) {}".format(state_name, city_id, city_name))

    session.close()
