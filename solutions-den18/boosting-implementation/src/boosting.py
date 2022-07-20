import numpy as np
from sklearn.dummy import DummyRegressor
from sklearn.tree import DecisionTreeRegressor

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
