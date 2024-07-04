#!/usr/bin/python3
'''
Class definition for Base model and State class
'''

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Database configuration
username = 'your_username'
password = 'your_password'
host = 'localhost'
port = 3306
database = 'your_database'

db_url = f'mysql+mysqldb://{username}:{password}@{host}:{port}/{database}'

# Create engine
engine = create_engine(db_url, echo=True)

# Declare a mapping
Base = declarative_base()


class State(Base):
    """
    Class definition of a State that inherits from Base
    and links to the MySQL table 'states'
    """
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True,
                unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)


# Create all tables in the engine
Base.metadata.create_all(engine)
