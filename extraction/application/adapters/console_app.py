import json
import os
import sys

from domain.extract_jobs import extract_jobs


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

    def extract_jobs_adapter(self) -> None:
        request = {
            "Keyword": self.arguments[1],  # Need documentation
            "DatePosted": int(self.arguments[2]),
            "LocationName": self.arguments[3],
            "Page": 0,
            "ResultsPerPage": 100
        }
        extract_jobs(request, self.storage_service)

    def create_app(self) -> None:
        self.get_arguments()

        if self.arguments[0] == "extract_jobs":
            self.extract_jobs_adapter()

        else:
            raise Exception(f"The specified parameter {self.arguments[0]} is not recognised")

