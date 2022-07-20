from sklearn.metrics import (roc_curve, auc, mean_squared_error, r2_score, accuracy_score, confusion_matrix)
from sklearn.model_selection import (train_test_split, cross_val_score, KFold, GridSearchCV, RandomizedSearchCV)
from processing import pre_processing, eda_processing
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from scipy import (interpolate, integrate)
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
plt.style.use('bmh')

def rmse(y_true, y_predict):
    return np.sqrt(mean_squared_error(y_true, y_predict))

def crossVal(X, y, k, threshold=0.75):
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
        #metrics
        train_accuracy.append(accuracy_score(y_train, y_hat_train))
        test_accuracy.append(accuracy_score(y_test, y_hat_test))

    #np.mean(test_errors), np.mean(train_errors), np.mean(test_r2), np.mean(train_r2)
    return np.mean(train_accuracy), np.mean(test_accuracy)

def we_will_roc_you(X,y):
    model = RandomForestClassifier(max_features='log2', min_samples_leaf=10,
                                    min_samples_split=4, random_state=1)

    X_train, X_test, y_train, y_test = train_test_split(X,y)
    model.fit(X_train,y_train)
    probabilities = model.predict_proba(X_test)[:,1]

    fpr, tpr, thresholds = roc_curve(y_test, probabilities)
    x = np.linspace(0,1, 100)
    fig, ax = plt.subplots(1, figsize=(10,6))
    ax.plot(fpr, tpr, color='firebrick')
    ax.plot(x, x, linestyle='--', color ='black', label='Random Guess')
    ax.set_xlabel('False Positive Rate (FPR)', fontsize=16)
    ax.set_ylabel('True Positive Rate (TPR)', fontsize=16)
    ax.set_title('ROC Curve for Random Forest')
    plt.legend()
    plt.savefig('../images/roccurve.png',  bbox_inches='tight')

    return thresholds[fpr>0.3][0]


def grid_search(X_train, y_train):
    rf = RandomForestClassifier(n_estimators=100,
                                n_jobs=-1,
                                random_state=1)

    rf.fit(X_train, y_train)

    random_forest_grid = {'max_depth': [3, 5, None],
                        'max_features': ['sqrt', 'log2', None],
                        'min_samples_split': [2, 4],
                        'min_samples_leaf': [1, 5, 10, 15],
                        'bootstrap': [True, False],
                        'n_estimators': [20, 40, 50, 100, 200],
                        'random_state': [1]}

    rf_gridsearch = RandomizedSearchCV(RandomForestClassifier(),
                                random_forest_grid,
                                n_iter = 200,
                                n_jobs=-1,
                                verbose=True,
                                scoring='accuracy')
    rf_gridsearch.fit(X_train, y_train)

    print("Random Forest best parameters:", rf_gridsearch.best_params_)

    best_rf_model = rf_gridsearch.best_estimator_

    return best_rf_model

def model(X_train, X_test, y_train, y_test):

    '''
    USE BEST FIT MODEL FROM GRID_SEARCH FUNCTION
    '''

    rfc = RandomForestClassifier(max_features='log2', min_samples_leaf=10,
                                    min_samples_split=4, random_state=1)

    rfc.fit(X_train, y_train)

    y_hat_testprob = rfc.predict_proba(X_test)[:,1]
    y_pred = (y_hat_testprob >= 0.55).astype(int)

    accuracy = accuracy_score(y_test, y_pred)

    return accuracy

def feature_importance(model, X):
    features = model.feature_importances_
    feat_pair = list(zip(X.columns, features))
    feat_pair.sort(key = lambda x: x[1], reverse = True)
    return feat_pair

def feature_importance_plot(feat_pair):
    fig, ax = plt.subplots(1, figsize=(10,6))
    ax.bar(range(len(feat_pair)), [val[1] for val in feat_pair], color='firebrick')
    plt.xticks(range(len(feat_pair)), [val[0] for val in feat_pair])
    plt.xticks(rotation=70)
    ax.set_xlabel('Features', fontsize=16)
    ax.set_xticklabels(["Driver Rating", "Surge %", "Weekday %",
                        "In King\'s Landing", "Ride Distance", "30 Day Trips",
                        "Rider Rating", "Phone Type", "Luxury Car", "In Astapor", "In Winterfell"])
    ax.set_ylabel('Proportion of Importance', fontsize=16)
    ax.set_title('Feature Importance for Random Forest Classification', fontsize=20)
    plt.tight_layout()
    plt.savefig('../images/featureimportance.png',  bbox_inches='tight')

def main():
    churn = pd.read_csv('../data/churn_train.csv')
    churn_test = pd.read_csv('../data/churn_test.csv')

    x = pre_processing(churn)
    train = eda_processing(x)

    x2 = pre_processing(churn_test)
    test = eda_processing(x2)

    #set x and y for training data
    X = train.drop('churned', axis=1).values
    y = train['churned'].values
    crossVal(X, y, 5, threshold=0.55)
    print(crossVal(X, y, 5, threshold=0.55))

    X_train, X_test, y_train, y_test = train_test_split(X,y)

    best_rf_model = grid_search(X_train, y_train)
    print(f'This is the best random forest model: {best_rf_model}')

    #USE BEST VALUES FROM GRID SEARCH
    accuracy = model(X_train, X_test, y_train, y_test)
    print(accuracy)

    y = test['churned'].values
    X = test.drop('churned',axis=1).values
    X_df = test.drop('churned', axis=1)

    pairs = feature_importance(model, X_df)

    print(sum(x[1] for x in pairs))

    #ROC curve and thresholds
    print(we_will_roc_you(X,y))

    print(feature_importance_plot(pairs))

if __name__ == '__main__':
    main()
