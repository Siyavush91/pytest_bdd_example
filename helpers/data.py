"""
Contains functions for interacting with data files.
"""
import logging
import jsonpickle


def write_data_into_json_file(file: str, obj: object):
    """
    Conver data from object into json file.

    :param file: json file.
    :param obj: object.
    """
    logging.info(f"Write data {obj} into file {file}")
    with open(file, 'w') as data:
        jsonpickle.set_encoder_options("json", indent=2)
        data.write(jsonpickle.encode(obj))


def load_from_json_file(file: str):
    """
    Convert data from json into object.

    :param file: json file.
    :return: object.
    """
    logging.info(f"Load data from file {file}")
    with open(file) as data:
        return jsonpickle.decode(data.read())
