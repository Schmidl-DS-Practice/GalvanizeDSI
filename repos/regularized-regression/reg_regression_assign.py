import numpy as np
import pandas as pd
from pandas.plotting import scatter_matrix

from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.model_selection import train_test_split, KFold
from sklearn.preprocessing import StandardScaler
from sklearn.base import clone
from sklearn.datasets import load_diabetes

import matplotlib.pyplot as plt
from src.utils import XyScaler

# linear_model.LinearRegression()
# linear_model.Ridge()
# linear_model.Lasso
# linear_model.ElasticNet
# alpha = lambda
# all 3 have: fit(X, y)
#             predict(X)
#             score(X, y)
# get mean and std. for each value in col subtract mean and divide std
# lambda of zero means not penalizing
# ElasticNet.cv
diabetes = load_diabetes()
X_raw = diabetes.data[:100]
y_raw = diabetes.target[:100]
X = pd.DataFrame(X_raw, columns=diabetes.feature_names)
y = pd.Series(y_raw, index=X.index)
# print(X.head())
# print(y.head())
# print(np.unique(X['sex']))
# print(X.mean())
# print(y.mean())

