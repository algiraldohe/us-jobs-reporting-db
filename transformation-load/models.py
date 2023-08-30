from sqlalchemy import Column, Integer, String, JSON, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base

# Define the model
Base = declarative_base()

# For alembic
metadata = Base.metadata


class Job(Base):
    __tablename__ = 'jobs'

    id = Column(Integer, primary_key=True)
    PositionTitle = Column(String)
    PositionURI = Column(String)
    PositionLocation = Column(JSON)
    PositionRemuneration = Column(JSON)
    RemoteIndicator = Column(Boolean)
    StorageFile = Column(String)
    DateAdded = Column(DateTime)
    UserAdded = Column(String)

    def __repr__(self):
        return f"id: {self.id}\
            , PositionTitle: {self.PositionTitle}\
            , StorageFile: {self.StorageFile}\
            , DateAdded: {self.DateAdded} "
