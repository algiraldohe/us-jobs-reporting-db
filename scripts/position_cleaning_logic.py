import json
import numpy as np


def extract_data_position_title(path:list, data:dict):
    """
    This function performs search in a dictionary(json)
    1. Identifies the field to extract.
    2. Get how many records where present in the data.
    3. Creates a dictionary to store the extracted occurrences.
    4. Navigates the keys and arrays in the json to find the matched field.

    Args:
        data (dict): Json file containing job posts.
        path (list): extracted path for the specific field within the json.

    Raises:
        KeyError: If an index is not mapped in the specified structure.
        KeyError: If a key was not found in the specified structure.

    Returns:
        dict: key = searched field, values = list(All the records fetched in the dictionary data.)
    """
    number_records = data['SearchResult']['SearchResultCount']
    field = path[-1]
    extracted_data = {f"{field}":[]}

    for index in range(0,number_records):
        # Define extraction logic for the field
        current = data
        for key in keys:

            if isinstance(current, dict):
                current = current.get(key)
            elif isinstance(current, list):
                try:
                    current = current[index]
                    current = current.get(key)
                except (ValueError, IndexError):
                    raise KeyError(f"Invalid list index '{key}'")
            else:
                raise KeyError(f"Structured in json file not recognised")

        extracted_data[field].append(current)

    return extracted_data

def find_location(data, target_location, is_remote:list):
    fetched_locations = []

    for i, record in enumerate(data):

        # Corroborate if last iteration inserted the record
        if (len(fetched_locations) == i-1):
            fetched_locations.append(None)
            print(i-1, None)

        # Avoid unnecessary serches with the RemoteIndicator field
        if is_remote[i]:
            location_text = "Anywhere in the U.S. (remote job)"
            fetched_locations.append(location_text)
            print(i , location_text)

        else:
            for entry in record:
                if (entry.get("LocationName") == target_location):
                    location_text = ", ".join([entry.get("LocationName") ,entry.get("CountryCode") ])
                    fetched_locations.append(location_text)
                    print(i , location_text)
                    break

    return fetched_locations

# Change the path for a file retrieved from the extraction service
filename = "/Users/alejandrogiraldoh/Development/us-jobs-reporting-db/file-storage/2023-08-30-us-jobs.json"
with open(filename, 'r') as json_file:
    jobs_data = json.load(json_file)

keys = ['SearchResult', 'SearchResultItems', 'MatchedObjectDescriptor', 'PositionLocation']
extracted_data = extract_data_position_title(keys, jobs_data)
size = len(extracted_data["PositionLocation"])
flags = np.random.choice([True, False], size=(size,))

target_location = "Chicago, Illinois"

filtered_data = list(map(lambda x: find_location(x, target_location, flags), extracted_data.values()))
print(len(filtered_data[0]))
