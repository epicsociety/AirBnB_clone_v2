#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
from models.city import City
import os

class State(BaseModel, Base):
    """ Contains the states table in the MySQL database
    contains attributes:
        __tablename__(str): MySQL table where state class wil be mapped
        name: name of the state
        cities: established state_city relationship
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", backref="state", cascade="delete")
    else:
        @property
        def cities(self):
            """Getter attribute cities"""
            city_instances = []
            all_cities = models.storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_instances.append(city)
            return city_instances
