import json
import os
import pandas as pd
from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Job

from contextlib import contextmanager


class DatabaseStorageService:
    def __init__(self) -> None:
        # Create the database connection
        username = os.environ.get("POSTGRES_USER")
        password = os.environ.get("POSTGRES_PASSWORD")
        localhost = os.environ.get("POSTGRES_HOST")
        dbname = os.environ.get("POSTGRES_DB")
        self.engine = create_engine(f'postgresql://{username}:{password}@{localhost}/{dbname}')
        Session = sessionmaker(bind=self.engine)
        self.session = Session()



    @contextmanager
    def session_scope(self) -> None:
        session = self.session
        try:
            yield session
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def save_data(self, data) -> None:
        """
        This method is in charge of handling the data response and storage in
        a file database.

        Args:
            data (dict): File retrieved from the file storage.

        """
        # Create a context manager for SQLAlchemy session
        with self.session_scope() as session:
            query = "SELECT * FROM jobs"
            data.to_sql(name="jobs", con=self.engine, index=False, if_exists="append")
            queried_df = pd.read_sql_query(query, con=session.bind)
            print("Data in POSTFRESQL \n")
            print(queried_df.info())

    def read_file(self, filestorage:str) -> dict:
        """_summary_

        Args:
            filestorage (str): _description_

        Returns:
            dict: _description_
        """
        # Get the datestamp to retrieve current's date file
        current_datetime = datetime.now()
        datestamp = current_datetime.strftime("%Y-%m-%d")
        filename = os.path.join(filestorage, f"{datestamp}-us-jobs.json")

        # Get the data from the file
        with open(filename, 'r') as json_file:
            jobs_data = json.load(json_file)

        return jobs_data

