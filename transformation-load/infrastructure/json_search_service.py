import json


def search_fields(json_obj, target_field, current_path=None):
    if current_path is None:
        current_path = []

    if isinstance(json_obj, dict):
        for key, value in json_obj.items():
            new_path = current_path + [key]
            if key == target_field:
                return new_path
            result = search_fields(value, target_field, new_path)
            if result:
                return result

    elif isinstance(json_obj, list):
        for index, value in enumerate(json_obj):
            new_path = current_path + [str(index)]
            result = search_fields(value, target_field, new_path)
            if result:
                return result

    return None


def filter_strings(input_list:list) -> list:
    """
    Return a proper list of field without considering the
    iterable structures.

    Args:
        input_list (list): _description_

    Returns:
        fields(list): _description_
    """

    # Delete int elements from list, containing the index
    # of the iterable json structure

    string_fields = []

    for field in input_list:
        try:
            int(field)

        except ValueError as e:
            string_fields.append(field)

    return string_fields


def find_json_path(json_object:dict, target_field:str) -> list:
    """_summary_

    Args:
        json_object (dict): _description_
        target_field (str): _description_

    Returns:
        list: _description_
    """
    # Search the path of the target field
    field_path = search_fields(json_object, target_field)

    # Remove indexes for iterable sections/structures
    corrected_field_path = filter_strings(field_path)

    return corrected_field_path

# with open("/Users/alejandrogiraldoh/Development/us-jobs-reporting-db/file-storage/2023-08-26-us-jobs.json", 'r') as json_file:
#     jobs_data = json.load(json_file)

# target_field = "PositionRemuneration"
# path = find_json_path(jobs_data, target_field)







