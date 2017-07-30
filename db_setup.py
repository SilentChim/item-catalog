

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
