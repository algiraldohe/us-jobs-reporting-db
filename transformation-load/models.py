from sqlalchemy import Column, Integer, String, JSON
from sqlalchemy.ext.declarative import declarative_base

# Define the model
Base = declarative_base()

# For alembic
metadata = Base.metadata


class Job(Base):
    __tablename__ = 'jobs'

    id = Column(Integer, primary_key=True)
    jobname = Column(String)
    location = Column(JSON)

    def __repr__(self):
        return f"id: {self.id}, jobname: {self.jobname}, location: {self.location}"
