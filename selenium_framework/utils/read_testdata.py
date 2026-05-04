import json

def get_login_data():
    with open("testdata/login_data.json") as f:
        return json.load(f)