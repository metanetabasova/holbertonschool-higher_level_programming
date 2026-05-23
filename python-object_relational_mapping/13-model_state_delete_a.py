#!/usr/bin/python3
"""Delete all State objects with a name containing the letter 'a'."""
import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            username, password, dbname
        ),
        pool_pre_ping=True,
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(State).filter(State.name.like("%a%")).delete(
        synchronize_session=False
    )
    session.commit()
    session.close()
