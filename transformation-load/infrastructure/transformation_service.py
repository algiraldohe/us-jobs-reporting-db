from infrastructure.json_search_service import find_json_path
import json


def extract_fields(data:dict) -> None:
    """
    Function in charge to extract the data from the specified fields.
    Params:
    fields_extraction_list (list): List of fields that will be extracted.

    Args:
        data (dict): JSON data from the jobs serach response.
    """
    fields_extraction_list = ["PositionTitle", "PositionURI", "PositionLocation", "PositionRemuneration"]

    field_path = {k: find_json_path(data, k) for k in fields_extraction_list}

    return field_path

