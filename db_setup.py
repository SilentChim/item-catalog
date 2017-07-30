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

class Feature(Base):
    """Class defines the table for the features in the database"""
    # Defines the name of the table
    __tablename__ = 'feature'
    user = relationship(User)
    # Mapper variables for feature attributes

class featureItem(Base):
    """Class defines the table for the items in the database"""
    # Defines the name of the table
    __tablename__ = 'feature_item'
    feature = relationship(Feature)
    user = relationship(User)
    # Mapper variables for feature item attributes


# End configuration code
engine = create_engine('sqlite:///featureitem.db')
Base.metadata.create_all(engine)
