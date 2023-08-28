import json
import os
import sys
from datetime import datetime

from domain.save_jobs import save_jobs
from infrastructure.read_data_service import read_file
from infrastructure.transformation_service import extract_fields_path, extract_fields_data



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

    def extract_jobs_data_adapter(self, data:dict) -> dict:
        """
        Extract data from the required fields
        """
        self.paths = extract_fields_path(data)

        extracted_data = list(map(lambda x: extract_fields_data(data=data, path=x), self.paths.values()))

        #return extracted_data

    def clean_jobs_adapter(self, data:dict) -> dict:
        # Perform cleaning and transformations operations
        target_location = self.arguments[1] # Needs documentation

        # Position


    def save_jobs_adapter(self) -> None:
        # Save the data into the databse
        pass

    def create_app(self) -> None:
        self.get_arguments()

        if self.arguments[0] == "save_jobs":
            jobs_data = self.get_jobs_adapter()
            extracted_jobs_data = self.extract_jobs_data_adapter(data=jobs_data)
            #formatted_jobs_data = self.clean_jobs_adapter(data=extracted_jobs_data)





