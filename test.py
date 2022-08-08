import requests

features = {
    "age": 30,
    "sex": "male",
    "bmi": 22,
    "children": 2,
    "smoker": "no",
    "region": "northwest"
}

url = 'http://localhost:9696/predict'


def request_prediction(url):
    response = requests.post(url, json=features)
    return response.json()


print(request_prediction(url))
