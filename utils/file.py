import os
from pathlib import Path


def get_project_root() -> Path:
    return Path(__file__).parent.parent


def add_allure_env(key, value):
    path = os.path.join(get_project_root(), 'allure-results', 'environment.properties')
    if not os.path.exists(path):
        with open(path, 'a') as f:
            f.write(f'{key} = {value}\n')
    else:
        dict_env = read_allure_env(path)
        if key in dict_env:
            if dict_env[key] != value:
                dict_env[key] = value
                with open(path, 'w') as f:
                    for item in dict_env:
                        f.write(f'{item} = {dict_env[item]}\n')

        else:
            with open(path, 'a') as f:
                f.write(f'{key} = {value}\n')


def read_allure_env(path):
    values = {}
    with open(path, 'r') as f:
        data = f.readlines()
    for item in data:
        values[item.split(' = ')[0]] = item.split(' = ')[1]
    return values
