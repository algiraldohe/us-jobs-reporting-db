import os
import sys
from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Job

# ----------
# import sys
# from dotenv import load_dotenv
# from infrastructure.database_storage_service import DatabaseStorageService
# from application.adapters.console_app import ConsoleApp

load_dotenv()

# if sys.argv[1] == "--console":
#     database_storage_service = DatabaseStorageService()
#     console_app = ConsoleApp(database_storage_service)  # Dependency injection
#     console_app.create_app()

# Create the database connection
username = os.environ.get("POSTGRES_USER")
password = os.environ.get("POSTGRES_PASSWORD")
localhost = os.environ.get("POSTGRES_HOST")
dbname = os.environ.get("POSTGRES_DB")
engine = create_engine(f'postgresql://{username}:{password}@{localhost}/{dbname}')
Session = sessionmaker(bind=engine)
session = Session()


# Create a new user
new_job = Job(jobname='Data Scientist', description="Test description")
session.add(new_job)
session.commit()

jobs = session.query(Job).all()
print(jobs)
