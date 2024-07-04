#!/usr/bin/python3
""" Define state model"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


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

