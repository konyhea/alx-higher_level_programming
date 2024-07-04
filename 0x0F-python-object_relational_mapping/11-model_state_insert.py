#!/usr/bin/python3
'''Import sections'''
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import create_engine
import sys


def main():
    '''Adds the State object “Louisiana” to the db'''

    username = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]

    db_url = f'mysql+mysqldb://{username}:{password}@localhost:3306/{db}'
    engine = create_engine(db_url)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()

    print(new_state.id)


if __name__ == "__main__":
    main()
