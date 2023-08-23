import os
from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Job

load_dotenv()


# Create the database connection
username = os.environ.get("POSTGRES_USER")
password = os.environ.get("POSTGRES_PASSWORD")
localhost = os.environ.get("POSTGRES_HOST")
dbname = os.environ.get("POSTGRES_DB")
engine = create_engine(f'postgresql://{username}:{password}@{localhost}/{dbname}')
Session = sessionmaker(bind=engine)
session = Session()


# Create a new user
new_job = Job(jobname='Data Engineer')
session.add(new_job)
session.commit()

jobs = session.query(Job).all()
print(jobs)
