#!/usr/bin/python3
'''Import sections'''
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
from sqlalchemy import create_engine
import sys


def main():
    '''List all state objects from the db'''
    # Extract command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]
    # Database URL
    db_url = f'mysql+mysqldb://{username}:{password}@localhost:3306/{db}'
    # Create the engine
    engine = create_engine(db_url)
    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # Create a Session
    session = Session()
    # Query all State objects, ordered by id
    states = session.query(State).order_by(State.id).all()
    # Print each state's id and name
    for state in states:
        print(f'{state.id}: {state.name}')
    # Close the session
    session.close()


if __name__ == "__main__":
    main()
