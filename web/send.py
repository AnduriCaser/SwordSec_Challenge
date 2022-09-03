import requests
import json
from pathlib import Path
import time

url = 'http://app:8000/users'
path = f'{Path(__file__).resolve().parent}/list'


def rq_send():
    for file in Path(path).glob('*.json'):
        f = open(file)
        json_data = json.load(f)
        r = requests.post(url, json=json_data)
        print(r.text)
    f = requests.post(url, json={'file': 'save.json'})
    print(f.text)


if __name__ == '__main__':
    rq_send()
