import json
import os

import requests
from requests.adapters import HTTPAdapter, Retry

API_KEY = os.environ.get("USAJOBS_KEY")
API_URL = "https://data.usajobs.gov/api/"
s = requests.Session()
retries = Retry(total=5, backoff_factor=0.1)
s.mount("http://", HTTPAdapter(max_retries=retries))

class USJobsService:
    """
    This class build the request, communicates to the API
    and retrieves and answer for the client.

    """

    def __init__(self) -> None:
        """ """

        self.headers = {"Authorization-Key": API_KEY}

    def search_data(self, request: dict) -> dict:
        """
        This method is in charge to fetch the data from the API.
        Retrieve API key from .env file, USAJOBS_KEY ans use it to perform
        the search based on the config parameters.

        Args:
            request (dict): parameters to build the request with

        Returns:
            dict: JSON with the response data
        """
        # Send the GET request
        response = s.get(f"{API_URL}/search", params=request, headers=self.headers)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()

            return data

        elif response.status_code == 401:
            message = f"""STATUS_CODE[{response.status_code}] - The request is not authorised.\
            Did you authenticate and provide the correct APIKEY [USAJOBS_KEY]"""

            raise Exception(message)

        else:
            message = f"""STATUS_CODE[{response.status_code}]  - The API is not working properly,\
            check your request or try again later. If the error persists, contact your\
            sys admin."""
            raise Exception(message)
