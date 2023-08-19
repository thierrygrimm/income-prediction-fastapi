# Script to train machine learning model.
import logging

import joblib
import pandas as pd
from sklearn.model_selection import train_test_split

from data import process_data
from model import train_model, compute_model_metrics

logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()

# Load in the data
logger.info("Loading the dataset")
data = pd.read_csv("./data/census.csv")

logger.info("Splitting the dataset 80:20")
train, test = train_test_split(data, test_size=0.20)

logger.info("Saving the train and test set")
train.to_csv("./data/train.csv", index=False)
test.to_csv("./data/test.csv", index=False)

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

# Process the train data with the process_data function.
logger.info("Processing the train data")
X_train, y_train, encoder, lb = process_data(
    train, categorical_features=cat_features, label="salary", training=True
)

# Train random forest model.
logger.info("Training the model")
model = train_model(X_train, y_train)
logger.info("Model successfully trained.")

# Process the test data with the process_data function.
logger.info("Processing the test data")
X_test, y_test, encoder, lb = process_data(
    test, categorical_features=cat_features, label="salary", training=False, encoder=encoder, lb=lb
)

logger.info("Computing model metrics")
precision, recall, fbeta, cl_report = compute_model_metrics(y_test, model.predict(X_test))
logger.info(f"Precision: {precision}")
logger.info(f"Recall: {recall}")
logger.info(f"fbeta: {fbeta}")
logger.info(cl_report)

# Save model
logger.info("Saving model as pickle")
joblib.dump(model, './model/rfc_model.pkl')

# Save OneHotEncoder
logger.info("Saving OneHotEncoder as pickle")
joblib.dump(encoder, './model/OHE.pkl')

# Save LabelBinarizer
logger.info("Saving LabelBinarizer as pickle")
joblib.dump(lb, './model/LB.pkl')
