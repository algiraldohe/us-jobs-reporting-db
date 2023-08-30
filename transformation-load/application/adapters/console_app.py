import os
import sys

from domain.transform_jobs import extract_fields_path, extract_fields_data, arrays_to_dataframe
from domain.save_jobs import save_jobs
from pymysql import OperationalError


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

    def store_jobs_adapter(self) -> dict:
        """
        Extract data from the required fields
        """
        filestorage = os.environ.get("FILESTORAGE")
        jobs_data = self.storage_service.read_file(filestorage=filestorage)

        self.paths = extract_fields_path(jobs_data)

        extracted_data = list(map(lambda x: extract_fields_data(data=jobs_data, path=x), self.paths.values()))

        jobs_dataframe = arrays_to_dataframe(data=extracted_data, filestorage=filestorage)
        try:
            save_jobs(jobs_dataframe, self.storage_service, **{"json_fields":["PositionLocation", "PositionRemuneration"]})
        except OperationalError as e:
            print(e)


    def create_app(self) -> None:
        self.get_arguments()

        if self.arguments[0] == "save_jobs":
            extracted_jobs_data = self.store_jobs_adapter()

        else:
            raise Exception(f"Operation {sys.argv[1]} not found")









