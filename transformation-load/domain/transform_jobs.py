from infrastructure.json_search_service import find_json_path
import pandas as pd


def navigate_dict(data, keys):
    current = data
    for key in keys:
        if key in current:
            current = current[key]
        else:
            raise KeyError(f"Key '{key}' not found in the current dictionary level.")
    return current

def extract_fields_path(data:dict) -> dict:
    """
    Function in charge to extract the data from the specified fields.
    Params:
    fields_extraction_list (list): List of fields that will be extracted.

    Args:
        data (dict): JSON data from the jobs serach response.
    """
    # Needs documentation
    fields_extraction_list = [
        "PositionTitle"
        , "PositionURI"
        , "PositionLocation"
        , "PositionRemuneration"
        , "RemoteIndicator"
        ]

    # Create dictionary with k=field, v=path in json
    fields_path = {k: find_json_path(data, k) for k in fields_extraction_list}

    return fields_path

def extract_fields_data(data:dict, path:list) -> dict:
    """
    This function performs search in a dictionary(json)
    1. Identifies the field to extract.
    2. Get how many records where present in the data.
    3. Creates a dictionary to store the extracted occurrences.
    4. Navigates the keys and arrays in the json to find the matched field.

    This function will take a dictionary that contains a field
    and the hierarchy structure where the field is aimed to be
    found in a json field, the hierarchy comes in form of a list

    Example nested structure with lists
    nested_data = {
        "level1": {
            "level2": [
                {
                    "value": "value1"
                },
                {
                    "value": "value2"
                }
            ]
        }
    }


    The data of the specific field in the json is found in the following way:


    data = ["level1", "level2", "1", "value"] eg. (data = "value2")

    Args:
        paths (dict): Dictionary with keys and paths

    Returns:
        dict: Structured formatted data for the specific field
    """
    number_records = data['SearchResult']['SearchResultCount']
    field = path[-1]
    extracted_data = {f"{field}":[]}

    for index in range(0,number_records):
        # Define extraction logic for the field
        current = data
        for key in path:

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


def arrays_to_dataframe(data:list) -> pd.DataFrame:
    """
    This function takes an array and creates a tabular format
    out of it to fit in a pd.DataFrame object.

    Args:
        data (list): _description_

    Returns:
        pd.DataFrame: _description_
    """
    combined_data_dict = {}
    for dictionary in data:
        combined_data_dict = {**combined_data_dict, **dictionary}

    jobs_data_df = pd.DataFrame(combined_data_dict)

    return jobs_data_df






