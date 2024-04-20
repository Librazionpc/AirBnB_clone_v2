#!/usr/bin/python3
""" State Module for HBNB project """
import os
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    
    if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', cascade='all, delete', backref='state')
    else:
        @property
        def cities(self):
            from models.city import City
            city = []
            for values in models.storage.all(City).values():
                if values.state_id == self.id:
                    city.append(values)
            return city
