import requests


def get_json(link):
    res = requests.get(link)
    return res.json()