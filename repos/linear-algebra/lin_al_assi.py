import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# stoch_mat = np.array([[0.7, 0.1, 0], [0.2, 0.9, 0.2], [0.1, 0, 0.8]])

# in_2004 = np.array([0.25, 0.20, 0.55])
# in_2009 = np.dot(stoch_mat, in_2004 )
# in_2014 = np.dot(stoch_mat, in_2009)

#print(in_2004, '\n')
#print(in_2009,'\n')
#print(in_2014, '\n')

iris = pd.read_csv('data/iris.txt')

print(iris.shape)
print(iris.head())
