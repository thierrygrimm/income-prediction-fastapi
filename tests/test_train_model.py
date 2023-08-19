import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)


def test_train_model_dataset():
    assert os.path.isfile("./data/census.csv")
