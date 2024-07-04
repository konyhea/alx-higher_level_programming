#!/usr/bin/python3
""" Define state model"""
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

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
