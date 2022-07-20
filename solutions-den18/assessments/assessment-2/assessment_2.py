import numpy as np
from scipy import stats
import pandas as pd
import random

# probability
def roll_the_dice(n_simulations = 1000):
    '''
    input: int
    output: float

    two unbiased, six sided, dice are thrown once and the sum of the showing
    faces is observed (so if you rolled a 3 and a 1, you would observe the sum,
    4). use a simulation to find the estimated probability that the total score
    is an even number or a number greater than 7.  your function should return 
    an estimated probability, based on rolling the two dice n_simulations times.
    '''
    total = 0
    num_repeats = 10000
    for i in range(num_repeats):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        score = die1 + die2
        if score % 2 == 0 or score > 7:
            total += 1
    return float(total) / num_repeats
    # with numpy operations
    # two_dice_sum = np.random.randint(1, 7, (2, 10000)).sum(axis=0)
    # return np.logical_or(two_dice_sum > 7, np.logical_not(two_dice_sum % 2)).mean()

# statistics
def calculate_t_test(sample1, sample2, type_i_error_rate):
    '''
    input: numpy array, numpy array
    output: float, boolean

    you are asked to evaluate whether the two samples come from a population
    with the same population mean.  return a tuple containing the p-value for
    the pair of samples and true or false depending if the p-value is
    considered significant at the provided type i error rate (i.e. false
    positive rate, i.e. alpha).
    '''
    _, pvalue = stats.ttest_ind(sample1, sample2)
    return pvalue, pvalue < type_i_error_rate

# pandas
def pandas_query(df):
    '''
    input: dataframe
    output: dataframe

    given a dataframe containing university data with these columns:
        name, address, website, type, size

    return the dataframe containing the average size for each university
    type ordered by average size in ascending order.
    '''
    return df.groupby('type').mean().sort_values(by='size')
    # alternative:
    # return df.groupby("type")["size"].mean().order()

def df_to_numpy(df, y_column):
    '''
    input: dataframe, string
    output: 2 dimensional numpy array, numpy array

    make the column named y_column into a numpy array (y) and make the rest of
    the dataframe into a 2 dimensional numpy array (x). return (x, y).

    e.g.
                a  b  c
        df = 0  1  3  5
             1  2  4  6
        y_column = 'c'

        output: np.array([[1, 3], [2, 4]]), np.array([5, 6])
    '''
    # if you use pop, you need to make a copy or the original dataframe will be
    # changed since dataframes are passed into functions by reference.
    dummy = df.copy()
    y = dummy.pop(y_column)
    return dummy.values, y.values

    # alternate:
    # y = df[y_column]
    # x = df.drop(y_column, axis=1)
    # return x.values, y.values

# numpy
def size_of_multiply(a, b):
    '''
    input: 2 dimensional numpy array, 2 dimensional numpy array
    output: tuple

    if matrices a (dimensions m x n) and b (dimensions p x q) can be
    multiplied (ab), return the shape of the result of multiplying them. use the
    shape function. do not actually multiply the matrices, just return the
    shape.

    if a and b cannot be multiplied, return none.
    '''
    if a.shape[1] == b.shape[0]:
        return a.shape[0], b.shape[1]
    return none

# sql
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
