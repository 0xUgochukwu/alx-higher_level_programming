#!/usr/bin/python3
"""
This module runs a script to deletes rows
matching a pattern from the states table
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    db = Session()

    for instance in db.query(State).filter(State.name.contains('a')):
        db.delete(instance)

    db.commit()
    db.close()
