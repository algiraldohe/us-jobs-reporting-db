from sqlalchemy import Column, Integer, String, JSON, Boolean
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

    def __repr__(self):
        return f"id: {self.id}, PositionTitle: {self.jobname}"
