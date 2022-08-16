import requests

features = {
    "age": 30,
    "sex": "male",
    "bmi": 23,
    "children": 1,
    "smoker": "yes",
    "region": "northwest"
}

url = 'http://localhost:9696/predict'


def request_prediction(url: object):
    response = requests.post(url, json=features)
    return response.json()


print(request_prediction(url))
