from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Define the model
Base = declarative_base()

# For alembic
metadata = Base.metadata


class Job(Base):
    __tablename__ = 'jobs'

    id = Column(Integer, primary_key=True)
    jobname = Column(String)
    description = Column(String)

    def __repr__(self):
        return f"id: {self.id}, jobname: {self.jobname}, description: {self.description}"
