#!/usr/bin/python3
'''Import sections'''
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import create_engine
import sys


def main():
    '''Changes the name of a State object from the database'''

    username = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]

    db_url = f'mysql+mysqldb://{username}:{password}@localhost:3306/{db}'
    engine = create_engine(db_url)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Retrieve the state with id = 2
    state = session.query(State).filter_by(id=2).first()
    if state:
        state.name = 'New Mexico'
        session.commit()


if __name__ == "__main__":
    main()
