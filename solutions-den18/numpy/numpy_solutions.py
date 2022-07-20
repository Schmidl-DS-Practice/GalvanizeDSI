import numpy as np
from typing import Tuple

# 1.
def column_vector(n: int) -> np.ndarray:
    return np.arange(1, n+1).reshape(n, 1)

# 2.
def random_array(t: Tuple[int]) -> np.ndarray:
    return np.random.uniform(size=t)

# 3.
def to_blue_and_red(x: np.ndarray) -> np.ndarray:
    colors = np.array(["red", "blue"])
    return colors[x]

# 4.
def compute_try_false_sums(x, b):
    return {
        True: np.sum(x[b]),
        False: np.sum(x[~b])
    }

# 5.
# First solution: np.where does this directly!
def select_from_two_arrays(x, y, b):
    return np.where(b, x, y)

# Second solution: Clever arithmetic and broadcasting.
def select_from_two_arrays_v2(x, y, b):
    return b * x + (1 - b) * y

# 6.
def sum_of_squared_differences(x, y):
    return np.sum((x - y) * (x - y))

# 7.
def row_or_column_means(X, label):
    if label == "row":
        return np.mean(X, axis=1)
    elif label == "column":
        return np.mean(X, axis=0)
    else:
        raise ValueError("label argument must be 'row' or 'column'")

# 8.
def ones_above_and_below_diagonal(n):
    x = np.zeros((n, n))
    # Fill ones *below* the main diagonal.
    np.fill_diagonal(x[1:, :], val=1.0)
    # Fill ones *above* the main diagonal.
    np.fill_diagonal(x[:, 1:], val=1.0)
    return x

# 9.
def checkerboard(n):
    # Our strategy here is to take every other row/column value and change it to a one.
    # Then do the same thing but starting one position ahead to fill in the remaining spots.
    """
    5x5 example:

    0 0 0 0 0     1 0 1 0 1     1 0 1 0 1
    0 0 0 0 0     0 0 0 0 0     0 1 0 1 0
    0 0 0 0 0 --> 1 0 1 0 1 --> 1 0 1 0 1
    0 0 0 0 0     0 0 0 0 0     0 1 0 1 0
    0 0 0 0 0     1 0 1 0 1     1 0 1 0 1
    
    """
    x = np.zeros((n, n))
    x[::2, ::2] = 1
    x[1::2, 1::2] = 1
    return n


# 10.
def ones_border(n):
    # It's easier to start with all ones and fill in the center!
    x = np.ones((n, n), dtype=int)
    x[1:-1, 1:-1] = 0
    return x

# 11.
def select_negative_columns(M):
     columns_contain_negatives = np.any(M < 0, axis=0)
     return M[:, columns_contain_negatives]

# 12.
def get_closest_idx(x, num):
    distance_to_number = np.abs(x - num)
    return np.argmin(distance_to_number)

# 13
def subtract_row_means(x):
    row_means = np.mean(x, axis=1)
    n_rows = x.shape[0]
    return x - row_means.reshape((n_rows, 1))

# 14
def cartesian_to_polar(x):
    r = np.sqrt(x[:, 0]**2 + x[:, 1]**2)
    theta = np.arctan2(x[: ,1], x[:, 0])
    polar = np.zeros(x.shape)
    polar[:, 0], polar[:, 1] = r, theta
    return polar

# 15
def smallest_angle(M, x):
    # Make sure that x is a column vector.
    x = x.reshape((-1, 1))
    # We're looking for angles, so we should make both x, and each row in M,
    # a unit vector.
    x_norm = x / np.linalg.norm(x)
    M_norm = M / np.linalg.norm(M, axis=1).reshape((-1, 1))
    # This matrix product gives the dot product of x with every row in M.
    cosines = M_norm @ x_norm
    # The angle is then the inverse cosine of the dot product, and we're
    # looking for the angle closest to zero.
    argmin_row = np.argmin(np.abs(np.arccos(cosines)))
    return M[argmin_row, :]
