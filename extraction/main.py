import os

import requests
from dotenv import load_dotenv

load_dotenv()


API_URL = "https://data.usajobs.gov/api/"
API_KEY = os.environ.get("USAJOBS_KEY")


headers = {"Authorization-Key": API_KEY}

# Parameters to be included in the URL
params = {
    "Keyword": "data engineering",
    "DatePosted": 3,
    "LocationName": ["Chicago, Illinois"],
}

# Send the GET request
response = requests.get(f"{API_URL}/search", params=params, headers=headers)

# Parse the JSON response
data = response.json()

print(data)
