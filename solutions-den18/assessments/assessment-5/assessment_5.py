import numpy as np

# Numpy
def boolean_indexing(arr, minimum):
    '''
    INPUT: NUMPY ARRAY, INT
    OUTPUT: NUMPY ARRAY
    (of just elements in "arr" greater or equal to "minimum")

    Return an array of only the elements of "arr"
    that are greater than or equal to "minimum"

    Ex:
    In [1]: boolean_indexing(np.array([[3, 4, 5], [6, 7, 8]]), 7)
    Out[1]: array([7, 8])
    '''
    return arr[arr >= minimum]

def reverse_index(arr, finRow, finCol):
    '''
    INPUT: NUMPY ARRAY, INT, INT
    OUTPUT: NUMPY ARRAY (of an upside down subset of "arr")

    Reverse the row order of "arr" (i.e. so the top row is on the bottom)
    and return the sub-matrix from coordinate [0, 0] up to
    (but not including) [finRow, finCol].

    Ex:
    In [1]: arr = np.array([[ -4,  -3,  11],
                            [ 14,   2, -11],
                            [-17,  10,   3]])
    In [2]: reverse_index(arr, 2, 2)
    Out[2]:
    array([[-17, 10],
           [ 14,  2]])

    Hint: this can be using two steps of slicing
    that can be combined into a one-liner.
    '''
    return arr[::-1][:finRow, :finCol]

# Decision Trees
def split_node(X, y, col, split_val):
    '''
    INPUT: NUMPY ARRAY, NUMPY ARRAY, INT, FLOAT
    OUTPUT: NUMPY ARRAY, NUMPY ARRAY, NUMPY ARRAY, NUMPY ARRAY

    Split a feature matrix X and the target array y into "left" and "right"
    arrays determined by splitting on "split_val" in col of the X matrix.
    The "left" matrices of X and y contain the rows corresponding to values in 
    col <= split value, while the "right" matrices contain the rows where
    col > split value.  Return the four arrays separately (see example
    below).

    You can assume that all columns in X are continuous values.  col is
    an integer (0 indexed) that indicates which column of X to use to split
    the X and y arrays.

    Return empty arrays for the left or right arrays if no values are returned.
    
    Ex:
    In [1]: X = np.array([[ 5.5,  2.4,  3.7],
                          [ 5.5,  2.3,  3.8],
                          [ 6.1,  3.0,  4.9],
                          [ 5.2,  3.5,  1.5],
                          [ 5.7,  2.6,  3.5]])
    
    In [2]: y = np.array([1, 1, 2, 0, 1])
    
    In [3]: X_left, y_left, X_right, y_right = split_node(X, y, 1, 2.6)

    In [4]: X_left
    Out[4]:
    array([[5.5, 2.4, 3.7],
           [5.5, 2.3, 3.8],
           [5.7, 2.6, 3.5]])
    
    In [5]: y_left
    Out[5]: array([1, 1, 1])

    '''
    left = X[:, col] <= split_val
    right = ~left
    return X[left], y[left], X[right], y[right]


def calculate_entropy(arr):
    '''
    INPUT: NUMPY ARRAY of binary values (0 and 1)
    OUTPUT: FLOAT

    Return the Shannon entropy of a numpy array containing only two classes
    (integers 0 and 1).

    You can assume that the array will always contain one or more values.
    '''
    # solution is for an arbitrary number of classes 
    num_val = len(arr) 
    classes = np.unique(arr)
    probs = [len(arr[arr==cls])/num_val for cls in classes]
    return -1*sum([p*np.log2(p) for p in probs])

# SQL

def market_density_per_state():
    '''
    INPUT: NONE
    OUTPUT: STRING

    Return a SQL statement which gives a table containing each state, number
    of people per farmers market (using the population number from 2010).
    If a state does not appear in the farmersmarket table, it should still
    appear in your result with a count of 0.
    '''

    return '''
             SELECT p.state, COALESCE(p.pop2010 / m.cnt, 0)
               FROM statepopulations p
               LEFT OUTER JOIN (
                 SELECT state, COUNT(1) AS cnt
                   FROM farmersmarkets 
                   GROUP BY state) m 
                 ON p.state=m.state
            ;
           '''

# Alternate queries for edification
#     return '''
#            -- Replace COALESCE from previous example with CASE WHEN
#            SELECT p.State, 
#                 CASE 
#                   WHEN m.cnt IS NULL THEN 0
#                   ELSE pop2010 / m.cnt 
#                 END
#               FROM statepopulations p
#                 LEFT OUTER JOIN (
#                   SELECT state, COUNT(1) AS cnt
#                     FROM farmersmarkets
#                     GROUP BY state) m 
#                   ON p.State = m.state
#             ;
#            '''
# 
#     return '''
#            -- Remove subquery from previous example
#            -- Flip join order
#            SELECT p.State, 
#                CASE 
#                  WHEN COUNT(FMID) = 0 THEN 0 
#                  ELSE pop2010 / COUNT(FMID) 
#                END
#              FROM farmersmarkets m
#                RIGHT OUTER JOIN statepopulations p 
#                  ON p.State = m.state
#              GROUP BY p.State, pop2010
#            ;
#            '''
# 
#     return '''
#            -- Replace CASE WHEN from previous example with COALESCE
#            -- Use FULL JOIN instead of LEFT JOIN or RIGHT JOIN
#            SELECT p.State, COALESCE(pop2010 / NULLIF(COUNT(FMID), 0), 0) 
#              FROM farmersmarkets m
#                FULL JOIN statepopulations p 
#                  ON p.State = m.state
#              GROUP BY p.State, pop2010
#            ;
#            '''
