import requests
import json

features = {
    "age": 30,
    "sex": "male",
    "bmi": 23,
    "children": 1,
    "smoker": "yes",
    "region": "northwest"
}

def request_prediction(url: object):
    response = requests.post(url, json=features)
    return response.json()

if __name__ == "__main__":
    host = "http://0.0.0.0:9696"
    url = f'{host}/predict'
    print(request_prediction(url))
