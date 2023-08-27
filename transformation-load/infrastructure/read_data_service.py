import os
import json
from datetime import datetime

def read_file(filestorage:str) -> dict:
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
