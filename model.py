import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import fbeta_score, precision_score, recall_score, classification_report
from sklearn.model_selection import GridSearchCV

from data import process_data


def train_model(X_train, y_train):
    """
    Trains a machine learning model and returns it.

    Inputs
    ------
    X_train : np.array
        Training data.
    y_train : np.array
        Labels.
    Returns
    -------
    model
        Trained machine learning model.
    """
    param_grid = {'n_estimators': [100, 125, 150, 175], 'max_depth': [75, 100, 125], 'criterion': ['gini', 'entropy']}

    # Optimal hyperparameters after sweep:
    # 'n_estimators': 150,
    # 'max_features': sqrt,
    # 'max_depth': 75,
    # 'criterion': 'gini'

    rfc = RandomForestClassifier()
    cv_rfc = GridSearchCV(estimator=rfc, param_grid=param_grid, cv=5)

    cv_rfc.fit(X_train, y_train)
    return cv_rfc.best_estimator_


def compute_model_metrics(y, preds):
    """
    Validates the trained machine learning model using precision, recall, and F1.

    Inputs
    ------
    y : np.array
        Known labels, binarized.
    preds : np.array
        Predicted labels, binarized.
    Returns
    -------
    precision : float
    recall : float
    fbeta : float
    cl_report : str
    """
    fbeta = fbeta_score(y, preds, beta=1, zero_division=1)
    precision = precision_score(y, preds, zero_division=1)
    recall = recall_score(y, preds, zero_division=1)
    cl_report = classification_report(y, preds)
    return precision, recall, fbeta, cl_report


def inference(model, X):
    """ Run model inferences and return the predictions.

    Inputs
    ------
    model : sklearn.ensemble.RandomForestClassifier
        Trained machine learning model.
    X : np.array
        Data used for prediction.
    Returns
    -------
    preds : np.array
        Predictions from the model.
    """

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
    encoder = joblib.load("model/OHE.pkl")
    lb = joblib.load('model/LB.pkl')

    X_t, _, _, _ = process_data(X, categorical_features=cat_features, training=False, encoder=encoder)

    pred = model.predict(X_t)
    cl = lb.inverse_transform(pred)[0]
    return cl
