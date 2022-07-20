import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import uniform
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, KFold, RandomizedSearchCV
from sklearn.naive_bayes import BernoulliNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (recall_score, f1_score,
                            plot_roc_curve, roc_auc_score, plot_confusion_matrix)
from datacleanup import X, y

def crossVal(X, y, k, threshold):
    kf = KFold(n_splits=k)
    train_accuracy = []
    test_accuracy = []
    for train, test in kf.split(X):
        # Split into train and test
        X_train, X_test, y_train, y_test = X[train], X[test], y[train], y[test]
        # Fit estimator
        model = RandomForestClassifier(max_features='log2', min_samples_leaf=10,
                        min_samples_split=4, random_state=1)
        model.fit(X_train, y_train)
        # Measure performance
        y_hat_trainprob = model.predict_proba(X_train)[:,1]
        y_hat_testprob = model.predict_proba(X_test)[:,1]
        y_hat_train = (y_hat_trainprob >= threshold).astype(int)
        y_hat_test = (y_hat_testprob >= threshold).astype(int)
        # metrics
        train_accuracy.append(recall_score(y_train, y_hat_train))
        test_accuracy.append(recall_score(y_test, y_hat_test))
    return np.mean(train_accuracy), np.mean(test_accuracy)

def scale_data(X,y):
    scaler= StandardScaler()
    standard_X= scaler.fit_transform(X)
    log_Xtrain, log_Xtest, log_ytrain, log_ytest = train_test_split(standard_X, y, shuffle= True, test_size= .25, random_state= 3)
    return log_Xtrain, log_Xtest, log_ytrain, log_ytest

def randomsearch(model):
    log_Xtrain, _, log_ytrain, _ = scale_data(X, y)
    mod = model
    penalty = ['l1', 'l2']
    C = uniform(loc=0, scale=4)
    hyperparameters = dict(C=C, penalty=penalty)
    clf = RandomizedSearchCV(mod, hyperparameters, random_state=1, n_iter=100, cv=5, verbose=0, n_jobs=-1)
    logreg = clf.fit(log_Xtrain, log_ytrain)
    best_params= "tuned hyperparameters :(best parameters) ", logreg.best_params_
    best_score= "recall :",logreg.best_score_
    return best_params, best_score

def random_forest(X_train, X_test, y_train, y_test):
    '''perform random forest classifier'''
    random_forest_grid = {'max_depth': [3, 5, None],
                            'max_features': ['sqrt', 'log2', None],
                            'min_samples_split': [2, 4],
                            'min_samples_leaf': [1, 7, 15],
                            'bootstrap': [True, False],
                            'n_estimators': [40, 50, 100],
                            'random_state': [1]}
    rf_gridsearch = RandomizedSearchCV(RandomForestClassifier(),
                                        random_forest_grid,
                                        n_iter = 200,
                                        n_jobs=-1,
                                        verbose=True,
                                        scoring='f1')
    rf_gridsearch.fit(X_train, y_train)
    print("Random Forest best parameters:", rf_gridsearch.best_params_)
    best_rf_model = rf_gridsearch.best_estimator_
    best_rf_model.fit(X_train, y_train)
    y_predict = (best_rf_model.predict_proba(X_test)[:, 1] >= 0.3).astype(bool)
    return y_predict

def bern_nb(X_train, X_test, y_train):
    '''perform bernoulli naive bayes'''
    bern_nb_mod = BernoulliNB()
    bern_nb_mod.fit(X_train, y_train)
    y_predict = (bern_nb_mod.predict_proba(X_test)[:, 1] >= 0.3).astype(bool)
    return y_predict 

def get_f_recall_score(ret):
    recall_list = []
    f_score_list = []
    recall = recall_score(y_test, ret)
    #recall_list.append(recall)    
    f_score = f1_score(y_test, ret)
    #f_score_list.append(f_score)
    return recall, f_score
    
def plot_roc(X_test, y_test):
    mod = RandomForestClassifier(random_state=1, n_estimators=100, min_samples_split=4,
                                    min_samples_leaf=1, max_features='log2', max_depth=None,
                                    bootstrap=False)
    mod.fit(X_train, y_train)
    plot_roc_curve(mod, X_test, y_test)
    plt.legend()
    # plt.title('Bernoulli Naive Bayes ROC Curve')
    # plt.savefig('../images/bern_nb_roc.png')
    
    plt.title('Random Forest ROC Curve')
    plt.savefig('../images/random_forest_roc.png')
    plt.show()
    return plt

def plot_conf_matrix(X_test, y_test):
    mod = RandomForestClassifier(random_state=1, n_estimators=100, min_samples_split=4,
                                    min_samples_leaf=1, max_features='log2', max_depth=None,
                                    bootstrap=False)
    mod.fit(X_train, y_train) 
    plot_confusion_matrix(mod, X_test, y_test)
    # plt.title('Bernoulli Naive Bayes Confusion Matrix')
    # plt.savefig('../images/bern_nb_con_matrix.png')
    plt.title('Random Forest ROC Curve')
    plt.savefig('../images/random_forest_con_matrix.png')
    plt.show()
    return plt

def feature_importance(final_model, df, title, xtitle, n):
    importances = final_model.feature_importances_[:n]
    std = np.std([final_model.feature_importances_ for tree in final_model.estimators_],
             axis=0)
    indices = np.argsort(importances)[::-1]
    features = list(df.columns[indices])
    _, ax = plt.subplots(figsize= (14,10))
    ax.bar(range(10), importances[indices], yerr=std[indices], color="blue", align="center")
    ax.set_xticks(range(10))
    ax.set_xticklabels(features, rotation = 90)
    ax.set_xlim([-1, 10])
    ax.set_xlabel(xtitle, size= 22)
    ax.set_title(title, size= 30)
    ax.tick_params(axis='both', which='major', labelsize=22)
    return None 

if __name__ == "__main__":
    X = X.values
    y = y.values

    ## split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y)
    ## model me babee
    #models = [BernoulliNB(), RandomForestClassifier()]
    # c_v = crossVal(X, y, k, threshold)
    #rf_mod = random_forest(X_train, X_test, y_train, y_test)    
    #bern_dawg_nb = bern_nb(X_train, X_test, y_train)    

    ## get best params for random forest
    # rando_for_values = randomsearch(models[1])
    # print(rando_for_values)
    
    # func_returns = [rf_mod[1], bern_dawg_nb]    
    #get_me_scores_list = []
    # for i in func_returns: # change bern_dawg_nb below to i for use with random forest
    #get_me_my_scores = get_f_recall_score(bern_dawg_nb)
    #get_me_my_scores2 = get_f_recall_score(rf_mod)
    #print(f'Naive Bayes: {get_me_my_scores}')
    #print(f'Random Forest: {get_me_my_scores2}')
    # get_me_scores_list.append(get_me_my_scores) 
    # print(get_me_scores_list)
    
    ## plot me babe
    labels = ('Fraud', 'Not Fraud')    
    # for m in models:
    plot_roc(X_test, y_test)
    plot_conf_matrix(X_test, y_test)    
    
