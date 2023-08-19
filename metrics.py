import logging
import joblib
import pandas as pd
import numpy as np
from model import compute_model_metrics
from data import process_data

logging.basicConfig(filename="slice_output.txt", level=logging.INFO, format="%(message)s")
logger = logging.getLogger()

# Load in the data
#logger.info("Loading the dataset")
test = pd.read_csv("./data/test.csv")

# Load in the OneHotEncoder, LabelBinarizer and Model
encoder = joblib.load("model/OHE.pkl")
lb = joblib.load("model/LB.pkl")
model = joblib.load("model/rfc_model.pkl")

# Categorical Features
cat_features = [
    "workclass",
    "education",
    "marital-status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "native-country",
]

# Metrics
# logger.info("Processing the test data")

# Process the test data with the process_data function.
X_test, y_test, encoder, lb = process_data(
    test, categorical_features=cat_features, label="salary", training=False, encoder=encoder, lb=lb
)

for cat in ["workclass", "race", "sex", "relationship"]:
    logger.info(f"Category {cat}:")
    logger.info("\n")
    for val in test[cat].unique():
        X_slice, y_slice, encoder, lb = process_data(
            test[test[cat] == val], categorical_features=cat_features, label="salary", training=False, encoder=encoder, lb=lb
        )

        precision, recall, fbeta, _ = compute_model_metrics(y_slice, model.predict(X_slice))
        logger.info(f"{val}")
        logger.info(f"Precision: {precision.round(3)}, Recall: {recall.round(3)}, fbeta: {fbeta.round(3)}")
        logger.info("\n")
    logger.info("_____________________________________________________________")
    logger.info("\n")
