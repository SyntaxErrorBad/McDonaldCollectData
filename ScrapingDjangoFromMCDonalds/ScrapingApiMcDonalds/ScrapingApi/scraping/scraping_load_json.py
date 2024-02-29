import json
from django.conf import settings


def load_data_from_json_file():
    with open(settings.NAME_OF_JSON_FILE, 'r', encoding = 'utf-8') as file:
        data = json.load(file)
    return data