#!/usr/bin/python3
"""
Lists all State objects from the database.
Usage: ./7-model_state_fetch_all.py <mysql_username> <mysql_password> <database_name>
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}",
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id.asc()).all():
        print(f"{state.id}: {state.name}")

    session.close()
