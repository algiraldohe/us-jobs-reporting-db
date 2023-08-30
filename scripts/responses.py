CONFLICT_RESPONSE = {
    "status": "ERROR",
    "code": 409,
    "message": "CONFLICT: The {} you are trying to create already exists",
    "error_code": "object_already_exists",
    "details": {
        "field": "{}",
        "value": "{}"
    }
}

SUCCESS_RESPONSE = {
    "status": "SUCCESS",
    "code": 200,
    "message": "Operation performed successfully. {}",
    "data": {}

}

SUCCESS_CREATION_RESPONSE = {
    "status": "SUCCESS"
    , "code": 201
    , "message": "Operation performed successfully. {}"
    , "data": {}
}

NOT_ACCEPTABLE_RESPONSE = {
    "status": "ERROR",
    "code": 409,
    "message": "Operation failed. {}",
    "data": {}
}

BAD_REQUEST_RESPONSE = {
    "status": "ERROR",
    "code": 400,
    "message": "Operation failed. {}",
    "data": {}
}

NOT_FOUND_RESPONSE = {
    "status": "ERROR",
    "code": 404,
    "message": "Operation failed. {}",
    "data": {}
}
