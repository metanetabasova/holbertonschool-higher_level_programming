#!/usr/bin/python3
"""
List all State objects that contain the letter 'a' from the database.

Usage:
    ./9-model_state_filter_a.py <mysql_username> <mysql_password> <database_name>
"""
import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

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

    states = (
        session.query(State)
        .filter(State.name.like("%a%"))
        .order_by(State.id)
        .all()
    )

    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()
