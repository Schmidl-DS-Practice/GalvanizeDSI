from DecisionTree import DecisionTree
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd

class RandomForest(object):
    '''A Random Forest class'''

    def __init__(self, num_trees, num_features):
        '''
           num_trees:  number of trees to create in the forest:
        num_features:  the number of features to consider when choosing the
                           best split for each node of the decision trees
        '''
        self.num_trees = num_trees
        self.num_features = num_features
        self.forest = None

    def fit(self, X, y):
        '''
        X:  two dimensional numpy array representing feature matrix
                for test data
        y:  numpy array representing labels for test data
        '''
        self.forest = self.build_forest(X, y, self.num_trees,
                                        self.num_features)

    def build_forest(self, X, y, num_trees, num_features):
        '''
        Return a list of num_trees DecisionTrees built using bootstrap samples
        and only considering num_features features at each branch.
        '''
        pass
        forest = []
        for i in range(num_trees):
            samps = np.random.choice(X.shape[0], X.shape[0], replace=True)
            sample_X = np.array(X[samps])
            sample_y = np.array(y[samps])
            dt = DecisionTree(num_features=self.num_features)
            dt.fit(sample_X, sample_y)
            forest.append(dt)
        return forest

    def predict(self, X):
        '''
        Return a numpy array of the labels predicted for the given test data.
        '''
        pass

    def score(self, X, y):
        '''
        Return the accuracy of the Random Forest for the given test data and
        labels.
        '''
        pass

if __name__ == '__main__':
    df = pd.read_csv('../data/playgolf.csv')
    y = df.pop('Result').values
    X = df.values
    X_train, X_test, y_train, y_test = train_test_split(X, y)

    rf = RandomForest(num_trees=10, num_features=2)
    rf.fit(X_train, y_train)
    y_predict = rf.predict(X_test)
    #print("score:", rf.score(X_test, y_test))

    dt = DecisionTree(num_features=5)
    dt.fit(X_train, y_train)
    predicted_y = dt.predict(X_test)
    #print(dt)
    
    bf = rf.build_forest(X, y, 10, 5)
    print(bf)