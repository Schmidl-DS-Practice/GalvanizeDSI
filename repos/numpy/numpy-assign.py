import numpy as np

#1
def col_vec(n):
    return np.arange(0, n).reshape(n,1)

#2
def array(s,t):
    return np.random.uniform(size=(s,t))

#3
def int_num_arr(arr):
    colors = np.array(['red', 'blue'])
    return colors[arr]

#4
def sum_of_data(x,b):
    return np.sum(x[b]), np.sum(x[~b])

#5
def sel_one_of_two(x,y,b):
    return np.where(b,x,y)

#6
def sum_of_sq_diff(x,y):
    return np.sum((x-y)**2)

#7
def row_col_mean(a, label):
    #label must be 1 or 0
    return np.mean(a, axis=label)

#8
def ones_above_and_below_diag(n):
    