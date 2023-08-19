import os
import sys

import joblib
import pandas as pd
import pytest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from data import process_data


@pytest.fixture(scope='session')
def data():
    input_data = {
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
    return pd.DataFrame([input_data])


@pytest.fixture(scope='session')
def ohe():
    ohe = joblib.load("model/OHE.pkl")
    return ohe


@pytest.fixture(scope='session')
def lb():
    lb = joblib.load('model/LB.pkl')
    return lb


@pytest.fixture(scope='session')
def cat_features():
    cat_features = [
        "workclass",
        "education",
        "marital-status",
        "occupation",
        "relationship",
        "race",
        "sex",
        "native-country"
    ]
    return cat_features


@pytest.fixture(scope='session')
def expected_output():
    expected = [[5.0000e+01, 7.7516e+04, 2.0000e+01, 1.0000e+06, 0.0000e+00, 5.0000e+01,
                 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 1.0000e+00,
                 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
                 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
                 0.0000e+00, 0.0000e+00, 0.0000e+00, 1.0000e+00, 0.0000e+00, 0.0000e+00,
                 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 1.0000e+00,
                 0.0000e+00, 0.0000e+00, 0.0000e+00, 1.0000e+00, 0.0000e+00, 0.0000e+00,
                 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
                 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
                 1.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
                 0.0000e+00, 0.0000e+00, 0.0000e+00, 1.0000e+00, 0.0000e+00, 1.0000e+00,
                 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
                 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 1.0000e+00,
                 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
                 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
                 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
                 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
                 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00]]
    return expected


def test_data_process_data_y(data, ohe, lb, cat_features):
    X, y, encoder, lb = process_data(data, categorical_features=cat_features, label=None, training=False, encoder=ohe,
                                     lb=lb)
    assert y.size == 0


def test_data_process_data_x(data, ohe, lb, cat_features, expected_output):
    X, y, encoder, lb = process_data(data, categorical_features=cat_features, label=None, training=False, encoder=ohe,
                                     lb=lb)
    assert (X == expected_output).all()


def test_data_process_data_encoder(data, ohe, lb, cat_features):
    X, y, encoder, lb = process_data(data, categorical_features=cat_features, label=None, training=False, encoder=ohe,
                                     lb=lb)
    assert encoder == ohe


def test_data_process_data_label_binarizer(data, ohe, lb, cat_features):
    X, y, encoder, LB = process_data(data, categorical_features=cat_features, label=None, training=False, encoder=ohe,
                                     lb=lb)
    assert LB == lb
