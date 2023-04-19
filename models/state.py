#!/usr/bin/python3
""" State Module for HBNB project """
from base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ Contains the states table in the MySQL database
    contains attributes:
        __tablename__(str): MySQL table where state class wil be mapped
        name: name of the state
        cities: established state_city relationship
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="delete")
