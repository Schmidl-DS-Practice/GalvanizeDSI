import pandas as pd
from itertools import izip
from DecisionTreePruning import DecisionTreePruning


def test_tree(filename):
    df = pd.read_csv(filename)
    y = df.pop('Result').values
    X = df.values
    print X
    
    #tree = DecisionTree(leaf_size=10, depth=5, same_ratio=0.8, error_threshold=0.1)
    tree = DecisionTreePruning()
    tree.fit(X, y, df.columns)
    tree.prune(X, y)
    print tree

    y_predict = tree.predict(X)
    print '%26s   %10s   %10s' % ("FEATURES", "ACTUAL", "PREDICTED")
    print '%26s   %10s   %10s' % ("----------", "----------", "----------")
    for features, true, predicted in izip(X, y, y_predict):
        print '%26s   %10s   %10s' % (str(features), str(true), str(predicted))


if __name__ == '__main__':
    test_tree('data/playgolf.csv')
