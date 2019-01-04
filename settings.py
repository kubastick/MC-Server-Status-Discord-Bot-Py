import json


def token():
    json_data = open('./static/settings.json').read()
    data = json.loads(json_data)
    return data['token']
