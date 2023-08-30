import pandas as pd
import numpy as np
import json
from contextlib import contextmanager




def dict_to_json(data:pd.DataFrame, columns:list) -> pd.DataFrame:
    for column in columns:
        number_records = len(data[column].index)

        # Create a boolean NumPy array of length = number_records
        bool_array = np.full(number_records, True)

        # Create a JSON object for the input dict in the specified column
        # This step is required to avoid issues with saving the data into POSTGRESQL
        data.loc[bool_array, column] = data.loc[bool_array, column].apply(lambda x: json.dumps(x))

    return data


def save_jobs(data:pd.DataFrame, storage_service, **kwargs) -> None:

    if not kwargs:
        pass

    else:
        nested_fields = kwargs['json_fields'] # Needs documentation
        data = dict_to_json(data, kwargs['json_fields'])

        storage_service.save_data(data)






