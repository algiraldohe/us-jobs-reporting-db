import json
import os
import sys
import pandas as pd
from datetime import datetime

from domain.transform_jobs import extract_fields_path, extract_fields_data
from domain.save_jobs import save_jobs
from infrastructure.read_data_service import read_file


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

    # def get_jobs_adapter(self) -> None:
    #     filestorage = os.environ.get("FILESTORAGE")

    #     jobs_data = read_file(filestorage=filestorage)
    #     return jobs_data

    def store_jobs_adapter(self) -> dict:
        """
        Extract data from the required fields
        """
        filestorage = os.environ.get("FILESTORAGE")
        jobs_data = read_file(filestorage=filestorage)

        self.paths = extract_fields_path(jobs_data)

        extracted_data = list(map(lambda x: extract_fields_data(data=jobs_data, path=x), self.paths.values()))

        return extracted_data


    def create_app(self) -> None:
        self.get_arguments()

        if self.arguments[0] == "save_jobs":
            extracted_jobs_data = self.store_jobs_adapter()









