from sklearn.datasets import load_boston
import pandas as pd
import numpy as np
from sklearn.dummy import DummyRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split

def load_split_data():

    boston = load_boston()
    # House Prices
    y = boston.target
    # The other 13 features
    X = boston.data

    X_train, X_test, y_train, y_test = train_test_split(X, y)
    return X_train, X_test, y_train, y_test


class GradientBoostedRegressor:
    """A gradient boosting class
    """
    def __init__(self, n_estimators=100, learning_rate=0.1):
        self.n_estimators = n_estimators
        self.learning_rate = learning_rate
        self.estimators = []

    def fit(self, X, y):
        dummy = DummyRegressor()
        dummy.fit(X, y)
        self.estimators.append(dummy)
        for i in range(self.n_estimators):
            prediction = self.predict(X)
            target = self.learning_rate * (y - prediction)
            model = DecisionTreeRegressor()
            model.fit(X, target)
            self.estimators.append(model)

    def predict(self, X):
        predictions = np.zeros((len(self.estimators),
                                len(X)))
        for i, estimator in enumerate(self.estimators):
            predictions[i] = estimator.predict(X)

        return predictions.sum(axis=0)

if __name__ == '__main__':

    X_train, X_test, y_train, y_test = load_split_data()


