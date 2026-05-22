#!/usr/bin/python3
"""
Lists all State objects from the database hbtn_0e_6_usa.

Usage:
    ./7-model_state_fetch_all.py <mysql_username> <mysql_password> <database_name>
"""
import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State


def main():
    if len(sys.argv) != 4:
        return

    user = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(user, password, dbname),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id.asc()).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()


if __name__ == "__main__":
    main()
