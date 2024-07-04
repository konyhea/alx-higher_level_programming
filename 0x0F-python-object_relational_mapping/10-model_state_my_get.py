#!/usr/bin/python3
'''Import sections'''
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import create_engine
import sys


def main():
    '''
    Write a script that prints the State object with the name 
    passed as argument from the database hbtn_0e_6_usa
    '''

    username = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]
    search_name = sys.argv[4]

    db_url = f'mysql+mysqldb://{username}:{password}\
        @localhost:3306/{db}'
    engine = create_engine(db_url)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = (
        session.query(State).filter(State.name == search_name)
        )
    if states.first():
        print(states.first().id)
    else:
        print("Not found")


if __name__ == "__main__":
    main()
