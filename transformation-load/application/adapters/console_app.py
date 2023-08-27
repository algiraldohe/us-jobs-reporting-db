import json
import os
import sys
from datetime import datetime

from domain.save_jobs import save_jobs
from infrastructure.read_data_service import read_file
from infrastructure.transformation_service import extract_fields



class ConsoleApp:
    """
    This class is in charge of handling the request from the user
    reading the parameters that come with it.
    """

    def __init__(self, storage_service) -> None:
        self.storage_service = storage_service

    def get_arguments(self) -> None:
        """
        This method takes the request with input parameters from
        the console, and build the search request.

        """
        self.arguments = sys.argv[2:]

    def get_jobs_adapter(self) -> None:
        filestorage = os.environ.get("FILESTORAGE")

        jobs_data = read_file(filestorage=filestorage)
        return jobs_data

    def clean_jobs_adapter(self, data:dict) -> None:
        """
        1. Extract required fields
        2. Standardise data types before ingestion
        """
        formatted_jobs_data = extract_fields(data)
        print(formatted_jobs_data)

        # Perform cleaning and transformations operations


    def save_jobs_adapter(self) -> None:
        # Save the data into the databse
        pass

    def create_app(self) -> None:
        self.get_arguments()

        if self.arguments[0] == "save_jobs":
            jobs_data = self.get_jobs_adapter()
            formated_jobs_data = self.clean_jobs_adapter(data=jobs_data)





