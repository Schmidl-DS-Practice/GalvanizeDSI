def num_pts_for_same_density(n1, d1, d2):
    '''
    INPUT: INT, INT, INT
    OUTPUT: FLOAT
    
    n1 represents the number of datapoints in a d1 dimensional space. Return
    n2, the number of datapoints required to achieve the same data density
    in the d2 dimensional space.
    '''
    return n1**(d2/d1)


def same_proportion_minority_class(X, y, test_size=0.2):
    '''
    INPUT: NUMPY ARRAY, NUMPY ARRAY
    OUTPUT: NUMPY ARRAY, NUMPY ARRAY, NUMPY ARRAY, NUMPY ARRAY

    Perform an 80:20 train-test split on the X and y data, returning:

    X_train, X_test, y_train, y_test in that order.

    However, you know that the target y is categorical (0 and 1) and
    there is a large class imbalance.  Perform the train-test split
    such that the proportion of the minority class is preserved
    in the train and test sets.
    '''
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size,
                                                        stratify=y)
    return X_train, X_test, y_train, y_test


def filtered_market_count():
    '''
    INPUT: NONE
    OUTPUT: STRING

    Return a SQL statement which gives the number of markets that do not have 
    'Farmers Market' in its name. Please only include markets in states with a 
    large population in 2010 (greater than 20,000,000).
    '''

    return '''SELECT COUNT(*)
                FROM farmersmarkets AS fm
                JOIN statepopulations AS sp
                ON sp.state = fm.State
                WHERE sp.pop2000 > 20000000 AND
                      fm.MarketName NOT LIKE '%Farmers Market%';
           '''


