import numpy as np
import pandas as pd
from collections import Counter
from scipy.spatial import distance


def euclidean_distance(a, b):
    """Compute the euclidean distance between two numpy arrays.

    Parameters
    ----------
    a: numpy array
    b: numpy array

    Returns
    -------
    distance: float
    """
    c = []
    
    for _ in range(10):
        a = np.random.rand(10)
        b = np.random.rand(10)       
        dist = distance.euclidean(a, b)
        c.append(dist)
    return np.sqrt(np.dot(a - b, a - b))

    
        


def cosine_distance(a, b):
    """Compute the cosine dissimilarity between two numpy arrays.

    Parameters
    ----------
    a: numpy array
    b: numpy array

    Returns
    -------
    distance: float
    """
    c = []
    
    for _ in range(20):
        a = np.random.rand(10)
        b = np.random.rand(10)       
        dist = distance.cosine(a, b)
        c.append(dist)
    return 1 - np.dot(a, b) / np.sqrt(np.dot(a, a) * np.dot(b, b))


def manhattan_distance(a, b):
    """Compute the manhattan (L1) distance between two numpy arrays.

    Parameters
    ----------
    a: numpy array
    b: numpy array

    Returns
    -------
    distance: float
    """
    c = []
    
    for _ in range(1):
        a = np.random.rand(10)
        b = np.random.rand(10)        
        dist = distance.cityblock(a, b)
        c.append(dist)
    return np.sum(np.abs(a - b))


class KNNRegressor:
    """Regressor implementing the k-nearest neighbors algorithm.

    Parameters
    ----------
    k: int, optional (default = 5)
        Number of neighbors that are included in the prediction.
    distance: function, optional (default = euclidean)
        The distance function to use when computing distances.
    """

    def __init__(self, k=5, distance=euclidean_distance, weighted=False):
        """Initialize a KNNRegressor object."""
        self.k = k
        self.distance = distance

    def fit(self, X, y):
        """Fit the model using X as training data and y as target values.

        According to kNN algorithm, the training data is simply stored.

        Parameters
        ----------
        X: numpy array, shape = (n_observations, n_features)
            Training data.
        y: numpy array, shape = (n_observations,)
            Target values.

        Returns
        -------
        self
        """
        self.X_train = X
        self.y_train = y
        

    def predict(self, X):
        """Return the predicted values for the input X test data.

        Assumes shape of X is [n_test_observations, n_features] where
        n_features is the same as the n_features for the input training
        data.

        Parameters
        ----------
        X: numpy array, shape = (n_observations, n_features)
            Test data.

        Returns
        -------
        result: numpy array, shape = (n_observations,)
            Predicted values for each test data sample.

        """
        pass


if __name__ == '__main__':
    e_d = euclidean_distance(np.random.rand(10), np.random.rand(10))
    c_s = cosine_distance(np.random.rand(10), np.random.rand(10))
    m_d = manhattan_distance(np.random.rand(10), np.random.rand(10))

    knn = KNNRegressor(k=3, distance=euclidean_distance)
    knn.fit(X, y)
    y_pred = knn.predict(X)

