## Fill each each function stub according to the docstring.
## Updated for Python 3

import numpy as np
import pandas as pd
import string
from collections import defaultdict

def max_lists(list1, list2):
    '''
    INPUT: list, list
    OUTPUT: list

    list1 and list2 have the same length. Return a list which contains the
    maximum element of each list for every index.
    '''
    return [max(i1, i2) for i1, i2 in zip(list1, list2)]

def get_diagonal(mat):
    '''
    INPUT: 2 dimensional list
    OUTPUT: list

    Given a matrix encoded as a 2 dimensional python list, return a list
    containing all the values in the diagonal starting at the index 0, 0.

    E.g.
    mat = [[1, 2], [3, 4], [5, 6]]
    | 1  2 |
    | 3  4 |
    | 5  6 |
    get_diagonal(mat) => [1, 4]

    You may assume that the matrix is nonempty.
    '''
    return [mat[i][i] for i in range(min(len(mat), len(mat[0])))]

def merge_dictionaries(d1, d2):
    '''
    INPUT: dictionary, dictionary
    OUTPUT: dictionary

    Return a new dictionary which contains all the keys from d1 and d2 with
    their associated values. If a key is in both dictionaries, the value should
    be the sum of the two values.
    '''
    d = d1.copy()
    for key, value in d2.items():
        d[key] = d.get(key, 0) + value
    return d
    # Another solution:
    # return {k: d1.get(k, 0) + d2.get(k, 0) for k in (set(d1) | set(d2))}

def matrix_multiplication(A, B):
    '''
    INPUT: LIST (of length n) OF LIST (of length n) OF INTEGERS,
            LIST (of length n) OF LIST (of length n) OF INTEGERS
    OUTPUT: LIST OF LIST OF INTEGERS
            (storing the product of a matrix multiplication operation)

    Return the matrix which is the product of matrix A and matrix B
    where A and B will be (a) integer valued (b) square matrices
    (c) of size n-by-n (d) encoded as lists of lists,  e.g.
    A = [[2, 3, 4], [6, 4, 2], [-1, 2, 0]] corresponds to the matrix
    | 2  3  4 |
    | 6  4  2 |
    |-1  2  0 |
    
    YOU MAY NOT USE NUMPY. Write your solution in straight python.
    '''

    n = len(A)
    result = []
    # iterate over the rows of A
    for i in range(n):
        row = []
        # iterate over the columns of B
        for j in range(n):
            total = 0
            # iterate ith row of A with jth column of B dot product
            for k in range(n):
                # k implements [ith row][jth column] element-wise dot product
                total += A[i][k] * B[k][j]
            # column j of row i
            row.append(total)
        # all columns j of row i completed
        result.append(row)
    # all rows done
    return result

### Pandas
# For each of these, you will be dealing with a DataFrame which contains median
# rental prices in the US by neighborhood. The DataFrame will have these
# columns:
# Neighborhood, City, State, med_2011, med_2014

def pandas_add_increase_column(df):
    '''
    INPUT: DataFrame
    OUTPUT: None

    Add a column to the DataFrame called 'Increase' which contains the 
    amount that the median rent increased by from 2011 to 2014.
    '''
    df['Increase'] = df['med_2014'] - df['med_2011']
    # Another solution:
    # df.eval('Increase = med_2014 - med_2011')


def pandas_max_rent(df):
    '''
    INPUT: DataFrame
    OUTPUT: DataFrame

    Return a new pandas DataFrame which contains every city and the highest
    median rent from that city for 2011 and 2014.
    Your DataFrame should contain these columns:
        City, State, med_2011, med_2014

    '''
    return df[['City', 'State', 'med_2011', 'med_2014']].groupby(['City', 'State']).max()

    # Another solution:
    # return df.groupby(['City', 'State']).max().reset_index()[['City', 'State', 'med_2011', 'med_2014']]

