import os
from pathlib import Path


def get_project_root() -> Path:
    return Path(__file__).parent.parent


def add_allure_env(key, value):
    reports_directory = os.path.join(get_project_root(), 'allure-results')
    path = os.path.join(reports_directory, 'environment.properties')
    if not os.path.exists(reports_directory):
        os.makedirs(reports_directory)
    if not read_allure_env(path, key):
        with open(path, 'a') as f:
            f.write(f'{key} = {value}\n')


def read_allure_env(path, key):
    try:
        with open(path, 'r') as f:
            data = f.readlines()
        for item in data:
            if item.split(' = ')[0] == key:
                return True
    except FileNotFoundError:
        return False
    return False
