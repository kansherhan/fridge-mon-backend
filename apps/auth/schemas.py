LOGIN_SCHEMA = {
    "username": {
        "type": "string",
        "minlength": 2,
        "maxlength": 30,
    },
    "password": {"type": "string"},
}

REGISTRATION_SCHEMA = {
    "first_name": {
        "type": "string",
        "minlength": 2,
        "maxlength": 30,
    },
    "last_name": {
        "type": "string",
        "minlength": 2,
        "maxlength": 30,
    },
    "username": {
        "type": "string",
        "minlength": 2,
        "maxlength": 30,
    },
    "password": {"type": "string"},
}
