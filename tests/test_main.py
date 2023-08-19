import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_main_api_get_root():
    with TestClient(app) as client:
        # Tests root
        r = client.get("/")
        assert r.status_code == 200
        assert r.json() == {"greeting": "Hello World!"}


def test_main_api_inference_positive_example():
    with TestClient(app) as client:
        # Example expected to be positive
        r = client.post("/predict",
                        json={"age": 50, "workclass": "Self-emp-inc", "fnlgt": 77516, "education": "Masters",
                              "education-num": 20, "marital-status": "Never-married", "occupation": "Adm-clerical",
                              "relationship": "Not-in-family", "race": "White", "sex": "Male", "capital-gain": 1000000,
                              "capital-loss": 0, "hours-per-week": 50, "native-country": "Germany"})
        assert r.status_code == 200
        assert r.json() == {"prediction": ">50K"}


def test_main_api_inference_negative_example():
    with TestClient(app) as client:
        # Example expected to be negative
        r = client.post("/predict", json={"age": 75, "workclass": "Never-worked", "fnlgt": 77516, "education": "9th",
                                          "education-num": 1, "marital-status": "Married-civ-spouse",
                                          "occupation": "Adm-clerical",
                                          "relationship": "Not-in-family", "race": "Black", "sex": "Female",
                                          "capital-gain": 0,
                                          "capital-loss": 100000, "hours-per-week": 0, "native-country": "Vietnam"})
        assert r.status_code == 200
        assert r.json() == {"prediction": "<=50K"}


def test_main_api_inference_false_format():
    with TestClient(app) as client:
        # Missing or impermissible values
        r = client.post("/predict", json={"age": 75, "marital-status": "Married"})
        assert r.status_code == 422
