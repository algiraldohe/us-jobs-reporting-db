import json
import os
from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Job


class DatabaseStorageService:
    def __init__(self) -> None:
        # Create the database connection
        username = os.environ.get("POSTGRES_USER")
        password = os.environ.get("POSTGRES_PASSWORD")
        localhost = os.environ.get("POSTGRES_HOST")
        dbname = os.environ.get("POSTGRES_DB")
        engine = create_engine(f'postgresql://{username}:{password}@{localhost}/{dbname}')
        Session = sessionmaker(bind=engine)
        self.session = Session()


    def save_data(self, data: dict) -> None:
        """
        This method is in charge of handling the data response and storage in
        a file database.

        Args:
            data (dict): File retrieved from the file storage.

        """
        pass
