import requests

TOKEN = 'AQAAAABXMS0NAADLW5dNtLp9MkXPj87byx8_WZE'
URL = 'https://cloud-api.yandex.net:443/v1/disk/resources'


def create_folder(path: str):
    params = {'path': path}
    headers = {'Content-Type': 'application/json',
               'Authorization': TOKEN}
    creature = requests.api.put(URL, headers=headers, params=params)
    return creature.status_code


def delete_folder(path: str):
    params = {'path': path}
    headers = {'Content-Type': 'application/json',
               'Authorization': TOKEN}
    removal = requests.api.delete(URL, headers=headers, params=params)
    return removal.status_code

