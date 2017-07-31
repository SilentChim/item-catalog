# Configuration code
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    """Class defines the table for the users in the database"""
    # Defines the name of the table
    __tablename__ = 'user'
    # Mapper variables for user attributes
    name = Column(String(80), nullable = False)
    email = Column(String(80), nullable = False)
    picture = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)

class Application(Base):
    """Class defines the table for the features in the database"""
    # Defines the name of the table
    __tablename__ = 'application'
    # Defines relationships with other tables
    user = relationship(User)
    # Mapper variables for feature attributes
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    name = Column(String(250), nullable = False)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id
        }

class Feature(Base):
    """Class defines the table for the items in the database"""
    # Defines the name of the table
    __tablename__ = 'feature'
    # Defines relationships with other tables
    application = relationship(Application)
    user = relationship(User)
    # Mapper variables for feature item attributes
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    application_id = Column(Integer,ForeignKey('application.id'))
    title = Column(String(80), nullable = False)
    description = Column(String(250))
    client = Column(String(80), nullable = False)
    client_priority = Column(Integer)
    target_date = Column(String(6), nullable = False)
    product_area = Column(String(80), nullable = False)

    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
            'title': self.title,
            'description': self.description,
            'id': self.id,
            'client': self.client,
            'client_priority': self.client_priority,
            'target_date': self.target_date,
            'product_area': self.product_area
        }


# End configuration code
engine = create_engine('sqlite:///application.db')
Base.metadata.create_all(engine)
