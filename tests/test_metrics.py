import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)


def test_metrics_testdata_file():
    assert os.path.isfile("./data/test.csv")


def test_metrics_OHE_file():
    assert os.path.isfile("model/OHE.pkl")


def test_metrics_LB_file():
    assert os.path.isfile("model/LB.pkl")


def test_metrics_RFC_model_file():
    assert os.path.isfile("model/rfc_model.pkl")
