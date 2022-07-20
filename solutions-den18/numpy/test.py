import numpy as np
import numpy_solutions as ns

def array_equal(a: np.ndarray, b: np.ndarray) -> bool:
    return np.all(a == b)

def test_column_vector():
    assert array_equal(ns.column_vector(1), np.array([[1]]))
    assert array_equal(ns.column_vector(3),
                       np.array([[1], [2], [3]]))

def test_random_array():
    def array_between_zero_and_one(a: np.ndarray) -> bool:
        return np.all((0 <= a) & (a <= 1))
    shapes = [(1, 1), (2, 2), (5, 5), (10, 5), (1, 1, 1), (2, 2, 2)]
    for shape in shapes:
        x = ns.random_array(shape)
        assert(x.shape == shape)
        assert(array_between_zero_and_one(x))

def test_to_blue_and_red():
    assert array_equal(ns.to_blue_and_red([0, 1, 0]),
                       np.array(["red", "blue", "red"]))
    assert array_equal(ns.to_blue_and_red(np.array([0, 0, 1, 0, 1])),
                       np.array(["red", "red", "blue", "red", "blue"]))
