import numpy as np


def h(b1, b2, x1, x2):
    value = 1 / (1 + np.exp(-(b1*x1 + b2*x2)))
    return value


def predict_proba(X, coeffs):
    """Calculate the predicted conditional probabilities (floats between 0 and
    1) for the given data with the given coefficients.

    Parameters
    ----------
    X: np.array of shape (n_samples, n_features)  
        The data (independent variables) to use for prediction.
    coeffs: np.array of shape (n_features, )
        The hypothesized coefficients.  Note that the shape of X, and coeffs

    Returns
    -------
    predicted_probabilities: 
        The conditional probabilities given the data and coefficients.
    """
    b1 = coeffs[0]
    b2 = coeffs[1]
    return [h(b1, b2, x1, x2) for (x1, x2) in X]


def predict(X, coeffs, thresh=0.5):
    """
    Calculate the predicted class labels (0 or 1) for the given data with the
    given coefficients by comparing the predicted probabilities to a given
    threshold.

    Parameters
    ----------
    X: np.array of shape (n_samples, n_features)  
        The data (independent variables) to use for prediction.
    coeffs: np.array of shape (n_features, )
        The hypothesized coefficients.  Note that the shape of X, and coeffs
        must align.
    thresh: float
        Threshold for classification.

    Returns
    -------
    predicted_class: int
        The predicted class.
    """
    ps = predict_proba(X, coeffs)
    return np.ndarray([1 if p >= thresh else 0 for p in ps])
    #return ps >= thresh


def cost(X, y, coeffs):
    """
    Calculate the total logistic cost function of the data with the given
    coefficients.

    Parameters
    ----------
    X: np.array of shape (n_samples, n_features)  
        The data (independent variables) to use for prediction.
    y: np.array of shape (n_samples, )
        The actual class values of the response.  Must be encoded as 0's and
        1's.  Also, must align properly with X and coeffs.
    coeffs: np.array of shape (n_features, )
        The hypothesized coefficients.  Note that the shape of X, y, and coeffs
        must align.

    Returns
    -------
    logistic_cost: float
        The value of the logistic cost function evaluated at the given
        coefficients.
    """
    h = predict_proba(X, y)

    a =  np.dot(y,  np.log(h))


    c = 1 - h

    b = np.dot((-y + 1), np.log(-h + 1) )




    val = -1 * ( a + b )
    return val

def gradient(X, y, coeffs):
    """
    Calculate the gradient of the logistic cost function with the given
    coefficients.

    Parameters
    ----------
    X: np.array of shape (n_samples, n_features)  
        The data (independent variables) to use for prediction.
    y: np.array of shape (n_samples, )
        The actual class values of the response.  Must be encoded as 0's and
        1's.  Also, must align properly with X and coeffs.
    coeffs: np.array of shape (n_features, )
        The hypothesized coefficients.  Note that the shape of X, y, and coeffs
        must align.

    Returns
    -------
    logistic_gradient: np.array of shape (n_features, )
        The gradient of the logistic cost function evaluated at the given
        coefficients.
    """
    pass



if __name__ == '__main__':
    X_sample = np.array([[0, 1], [2, 2], [3, 0]])
    y_sample = np.array([1, 0, 0])
    coeffs = np.array([1, -0.5])

    p = predict_proba(X_sample, coeffs)
    y_hat = predict(X_sample, coeffs)
    cost = cost(X_sample, y_sample, coeffs)

    print(cost)