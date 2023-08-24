import json
import os
from datetime import datetime


class LocalStorageService:
    def __init__(self) -> None:
        pass

    def save_data(self, data: dict) -> str:
        """
        This method is in charge of handling the data response and storage in
        a file storage system.

        Args:
            data (dict): Response data from the search performed.

        Returns:
            str: path where the file containing the data was saved.
        """
        # Set output path
        storage = "file-storage/"
        filestorage = os.path.join(os.getcwd(), storage)

        if not os.path.exists(filestorage):
            os.makedirs(filestorage)

        # Get the datestamp to name the file
        current_datetime = datetime.now()
        datestamp = current_datetime.strftime("%Y-%m-%d")
        filename = os.path.join(filestorage, f"{datestamp}-us-jobs.json")

        with open(filename, "w") as us_jobs_json:
            json.dump(data, us_jobs_json)
