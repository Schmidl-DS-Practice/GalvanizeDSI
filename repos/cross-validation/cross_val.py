from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import KFold
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
import numpy as np
from sklearn.datasets import load_boston
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression

boston = load_boston()
X = boston.data # housing features
y = boston.target # housing prices

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.6)

def rmse(true, predicted):
    return np.sqrt(mean_squared_error(true, predicted))

list1 = [3,5,6,7,9]
list2 = [9,6,3,5,7]
#print(mean_squared_error(list1, list2))


# Fit your model using the training set
reg = KNeighborsRegressor()
reg.fit(X_train, y_train)

# Call predict to get the predicted values for training and test set
train_predicted = reg.predict(X_train)
test_predicted = reg.predict(X_test)

# Calculate RMSE for training and test set
print( 'RMSE for training set ', rmse(train_predicted, y_train) )
print( 'RMSE for test set ', rmse(y_test, test_predicted) )


def crossVal(X_train, y_train, k):
    kf = KFold(n_splits=k)
    test_error = []
    linear = LinearRegression()
    for train, test in kf.split(X_train):
        linear.fit(X_train[train], y_train[train])
        
        predict = linear.predict(X_train[test])

        test_error.append(rmse(y_train[test], predict))
    
    return test_error

print(crossVal(X_train, y_train, 5))

print(cross_val_score(reg, X_train, y_train))





