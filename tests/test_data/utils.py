import os
import json
from config import Config


def get_test_data_from_json(json_file_name):
    """ Прочитать данные из json и вернуть словарь"""
    test_data_json = os.path.join(Config.TEST_DATA_DIR, json_file_name)
    with open(test_data_json, 'r') as f:
        test_data = json.load(f)
    return test_data

