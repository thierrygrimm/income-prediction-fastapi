import requests
import json

data = {
    "age": 50,
    "workclass": "Self-emp-inc",
    "fnlgt": 77516,
    "education": "Masters",
    "education-num": 20,
    "marital-status": "Never-married",
    "occupation": "Adm-clerical",
    "relationship": "Not-in-family",
    "race": "White",
    "sex": "Male",
    "capital-gain": 1000000,
    "capital-loss": 0,
    "hours-per-week": 50,
    "native-country": "Germany"
    }

r = requests.post("https://census-income-prediction.onrender.com/predict", data=json.dumps(data))

print(r.json())