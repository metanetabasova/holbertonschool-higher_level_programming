#!/usr/bin/python3
"""
Prints the first State object from the database.

Usage: ./8-model_state_fetch_first.py <mysql_username> <mysql_password> <database_name>
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

    first_state = session.query(State).order_by(State.id).first()

    if first_state is None:
        print("Nothing")
    else:
        print("{}: {}".format(first_state.id, first_state.name))

    session.close()
