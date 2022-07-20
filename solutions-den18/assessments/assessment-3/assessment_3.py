'''
* Fill each each function stub according to the docstring.
* To run the unit tests: Make sure you are in the root dir(assessment-4)
  Then run the tests with this command: "make test"
'''

import numpy as np
import pandas as pd
import random

# Numpy
def add_column(arr, col):
    '''
    INPUT: 2 DIMENSIONAL NUMPY ARRAY, NUMPY ARRAY
    OUTPUT: 2 DIMENSIONAL NUMPY ARRAY

    Return a numpy array containing arr with col added as a final column. You
    can assume that the number of rows in arr is the same as the length of col.

    E.g.  np.array([[1, 2], [3, 4]]), np.array([5, 6))
              ->  np.array([[1, 2, 5], [3, 4, 6]])
    '''
    # by no means the only solution
    return np.hstack((arr, col.reshape(len(col), 1)))

def only_positive(arr):
    '''
    INPUT: 2 DIMENSIONAL NUMPY ARRAY
    OUTPUT: 2 DIMENSIONAL NUMPY ARRAY

    Return a numpy array containing only the rows from arr where all the values
    in that row are positive.

    E.g.  np.array([[1, -1, 2], 
                    [3, 4, 2], 
                    [-8, 4, -4]])
              ->  np.array([[3, 4, 2]])

    Use numpy methods to do this, full credit will not be awarded for a python
    for loop.
    '''
    return arr[np.min(arr, 1) > 0]

# Pandas
def make_series(start, length, index):
    '''
    INPUTS: INT, INT, LIST (of length "length")
    OUTPUT: PANDAS SERIES (of "length" sequential integers
             beginning with "start" and with index "index")

    Create a pandas Series of length "length" with index "index"
    and with elements that are sequential integers starting from "start".
    You may assume the length of index will be "length".

    E.g.,
    In [1]: make_series(5, 3, ['a', 'b', 'c'])
    Out[1]:
    a    5
    b    6
    c    7
    dtype: int64
    '''
    return pd.Series(np.arange(length) + start, index=index)

# SQL
def sql_query():
    '''
    input: none
    output: string

    given a table named universities which contains university data with these
    columns:

        name, address, website, type, size

    return a sql query that gives the average size of each university type
    in ascending order.
    '''
    # your code should look like this:
    # return '''select * from universities;'''
    return '''select 
                type, 
                avg(size) as avg_size 
              from universities 
              group by type 
              order by avg_size;
           '''

def sql_count_neighborhoods():
    '''
    INPUT: None
    OUTPUT: string

    Return a SQL query that gives the number of neighborhoods in each city
    according to the rent table. Keep in mind that city names are not always
    unique unless you include the state as well, so your result should have
    these columns: city, state, cnt
    '''
    return '''SELECT city, state, COUNT(1) AS cnt
              FROM rent
              GROUP BY city, state;'''

def sql_highest_rent_increase():
    '''
    INPUT: None
    OUTPUT: string

    Return a SQL query that gives the 5 San Francisco neighborhoods with the
    highest rent increase.
    '''
    return '''SELECT neighborhood
              FROM rent
              WHERE city='San Francisco'
              AND rent.med_2014 - rent.med_2011 IS NOT NULL
              ORDER BY med_2014-med_2011 DESC LIMIT 5;'''

def sql_rent_and_buy():
    '''
    INPUT: None
    OUTPUT: string

    Return a SQL query that gives the rent price and buying price for 2014 for
    all the neighborhoods in San Francisco.
    Your result should have these columns:
        neighborhood, rent, buy
    '''
    return '''SELECT a.neighborhood, a.med_2014 AS rent, b.med_2014 AS buy
              FROM rent a
              JOIN buy b
              ON a.neighborhood=b.neighborhood AND a.city=b.city AND a.state=b.state
              WHERE a.city="San Francisco";'''

