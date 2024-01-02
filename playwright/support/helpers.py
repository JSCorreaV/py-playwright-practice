import json
from conftest import PROJECT_ROOT_DIR


def load_fixtures(filename):
    file_path = f'{PROJECT_ROOT_DIR}/fixtures/flights/{filename}'
    file = open(f'{file_path}', encoding='UTF-8')
    data = json.load(file)
    return data


def close_fixtures(file):
    file.close()
