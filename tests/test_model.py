import os
import sys

import joblib
import pandas as pd
import pytest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from model import compute_model_metrics, inference


@pytest.fixture(scope='session')
def data():
    input_data = {"age": 50, "workclass": "Self-emp-inc", "fnlgt": 77516, "education": "Masters", "education-num": 20,
                  "marital-status": "Never-married", "occupation": "Adm-clerical", "relationship": "Not-in-family",
                  "race": "White", "sex": "Male", "capital-gain": 1000000, "capital-loss": 0, "hours-per-week": 50,
                  "native-country": "Germany"}
    return pd.DataFrame([input_data])


@pytest.fixture(scope='session')
def model():
    model = joblib.load("model/rfc_model.pkl")
    return model


def test_model_compute_model_metrics():
    y = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
    preds = [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0]  # 2 FP, 3 FN, 6 TN, 5 TP
    precision, recall, fbeta, cl_report = compute_model_metrics(y, preds)

    assert recall == 5 / 8
    assert precision == 5 / 7
    assert fbeta == 2 / 3


def test_model_inference(data, model):
    out = inference(model, data)
    assert out == '>50K'
