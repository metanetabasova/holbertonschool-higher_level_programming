#!/usr/bin/python3
"""
Lists all State objects from the database.

Usage:
    ./7-model_state_fetch_all.py <mysql_username> <mysql_password> <database_name>
"""
import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State


if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        user, password, dbname
    )
    engine = create_engine(url, pool_pre_ping=True)

    # Make sure Base is used (avoids pycodestyle F401) and tables exist
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()
