#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import ForeignKey, Column, String
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains the table city
    contains the attributes:
        __tablename__(str): The table where the class City will be mapped
        name: name of the city
        state_id: The state_id where city is located
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    places = relationship("Place", backref="cities", cascade="all, delete")
