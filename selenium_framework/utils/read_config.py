import json

def read_config():
    with open("config/config.json") as f:
        return json.load(f)
