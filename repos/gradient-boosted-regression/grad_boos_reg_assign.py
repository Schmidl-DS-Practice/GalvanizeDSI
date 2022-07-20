from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import AdaBoostRegressor
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import numpy as np

def load_split_data():

    boston = load_boston()
    # House Prices
    y = boston.target
    # The other 13 features
    X = boston.data

    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.80, test_size=0.20,
                                                        random_state=1)
    return X_train, X_test, y_train, y_test

def cv_MSE_R2(estimator, X_train, y_train, k=5):
    
    MSE = cross_val_score(estimator, X_train, y_train, cv=k, scoring='neg_mean_squared_error') * -1
    
    R2 = cross_val_score(estimator, X_train, y_train, cv=k, scoring='r2')
    mean_mse = MSE.mean()
    mean_r2 = R2.mean()
    
    return mean_mse, mean_r2

def stage_score_plot(estimator, X_train, y_train, X_test, y_test):
    '''
    Parameters: estimator: GradientBoostingRegressor or AdaBoostRegressor
                X_train: 2d numpy array
                y_train: 1d numpy array
                X_test: 2d numpy array
                y_test: 1d numpy array

    Returns: A plot of the number of iterations vs the MSE for the model for
    both the training set and test set.
    '''
    # MSE_train = cross_val_score(estimator, X_train, y_train, cv=5, scoring='neg_mean_squared_error') * -1
    # MSE_test = cross_val_score(estimator, X_test, y_test, cv=5, scoring='neg_mean_squared_error') * -1
    # mean_train_mse = MSE_train.mean()
    # mean_test_mse = MSE_test.mean()
    
    estimator.fit(X_train, y_train)
    title = estimator.__class__.__name__ 
    train_score = np.zeros((estimator.n_estimators,))
    test_score = np.zeros((estimator.n_estimators, ))
    learn_rate = estimator.learning_rate

    for i, y_train_pred in enumerate(estimator.staged_predict(X_train)):
        train_score[i] = mean_squared_error(y_train, y_train_pred)

    for i, y_test_pred in enumerate(estimator.staged_predict(X_test)):
        test_score[i] = mean_squared_error(y_test, y_test_pred)

    plt.plot(train_score, label="{0} Train - learning rate {1}".format(
                                                                title, learn_rate))
    plt.plot(test_score, label="{0} Test  - learning rate {1}".format(
                                                      title, learn_rate), ls='--')
    plt.title(title, fontsize=16)
    plt.ylabel('MSE', fontsize=14)
    plt.xlabel('Iterations', fontsize=14)
    
       
if __name__ == '__main__':
    X_train, X_test, y_train, y_test = load_split_data()

    rf = RandomForestRegressor(n_estimators=100,
                            n_jobs=-1,
                            random_state=1)

    gdbr = GradientBoostingRegressor(learning_rate=0.1,
                                    loss='ls',
                                    n_estimators=100,
                                    random_state=1)

    abr = AdaBoostRegressor(DecisionTreeRegressor(),
                            learning_rate=0.1,
                            loss='linear',
                            n_estimators=100,
                            random_state=1)

    mse_rf, r2_rf = cv_MSE_R2(rf, X_train, y_train, k=5)
    # mse_r2_gdbr = cv_MSE_R2(gdbr,  X_train, y_train, k=5)
    # mse_r2_abr = cv_MSE_R2(abr, X_train, y_train, k=5)

    # print('random forest: ', mse_r2_rf)
    # print('gradientboostreg: ', mse_r2_gdbr)
    # print('AdaBoostRegressor: ', mse_r2_abr)

    gdbr_2 = GradientBoostingRegressor(learning_rate=1,
                                    loss='ls',
                                    n_estimators=100,
                                    random_state=1)

    #mse_r2_gdbr_2 = cv_MSE_R2(gdbr_2,  X_train, y_train, k=5)
    #print('GradientBoostingRegressor_2: ', mse_r2_gdbr_2)

    stage_score_plot(gdbr, X_train, y_train, X_test, y_test)
    #print('GDBR LR 0.1: ', mse_gdbr_3)
    stage_score_plot(gdbr_2, X_train, y_train, X_test, y_test)
    #print('GDBR LR 1: ', mse_gdbr_4)
    plt.hlines(mse_rf, xmin=0, xmax=100, label='Random Forest MSE', linestyles='dashdot')
    plt.tight_layout()
    plt.legend()
    plt.show()
