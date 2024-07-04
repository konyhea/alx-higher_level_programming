#!/usr/bin/python3
'''Import sections'''
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import create_engine
import sys


def main():
    '''
    Deletes all State objects with a name containing the letter
    a from the db
    '''

    username = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]
    db_url = f'mysql+mysqldb://{username}:{password}\
        @localhost:3306/{db}'
    engine = create_engine(db_url)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = (
        session.query(State).filter(State.name.like('%a%')).all()
        )
    for state in states:
        session.delete(state)
    session.commit()


if __name__ == "__main__":
    main()
