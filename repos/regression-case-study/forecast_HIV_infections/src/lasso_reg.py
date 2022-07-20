from sklearn.linear_model import Lasso, LinearRegression
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from utils import XyScaler
from sklearn.model_selection import KFold, train_test_split
import hiv_data_pipeline as pipe


def rss(y, y_hat):
    return np.mean((y  - y_hat)**2)

def cv(X, y, n_folds, alpha=0.5):
    kf = KFold(n_splits=n_folds)
    test_errors = []
    train_errors = []
    for train, test in kf.split(X):
        # Split into train and test
        X_cv_train, y_cv_train = X.iloc[train], y.iloc[train]
        X_cv_test, y_cv_test = X.iloc[test], y.iloc[test]
        #Standardize data
        standardizer = XyScaler()
        y_train_values = y_cv_train.to_numpy()
        standardizer.fit(X_cv_train, y_train_values)
        X_cv_train_std, y_cv_train_std = standardizer.transform(X_cv_train, y_train_values)
        X_cv_test_std, y_cv_test_std = standardizer.transform(X_cv_test, y_cv_test.to_numpy())
        # Fit estimator
        estimator = Lasso(alpha)
        estimator.fit(X_cv_train_std, y_cv_train_std)
        # Measure performance
        y_hat_train = estimator.predict(X_cv_train_std)
        y_hat_test = estimator.predict(X_cv_test_std)
        #metrics
        test_errors.append(rss(y_cv_train_std, y_hat_train))
        train_errors.append(rss(y_cv_test_std, y_hat_test))
    return np.mean(test_errors), np.mean(train_errors)

def train_at_various_alphas(X, y, alphas, n_folds=10, **kwargs):
    cv_errors_train = pd.DataFrame(np.empty(shape=(n_folds, len(alphas))),
                                     columns=alphas)
    cv_errors_test = pd.DataFrame(np.empty(shape=(n_folds, len(alphas))),
                                        columns=alphas)
    for alpha in alphas:
        train_fold_errors, test_fold_errors = cv(X, y, n_folds=n_folds, alpha=alphas)
        cv_errors_train.loc[:, alpha] = train_fold_errors
        cv_errors_test.loc[:, alpha] = test_fold_errors
    return cv_errors_train.mean(axis=0), cv_errors_test.mean(axis=0)


def get_optimal_alpha(mean_cv_errors_test):
    alphas = mean_cv_errors_test.index
    optimal_idx = np.argmin(mean_cv_errors_test.values)
    optimal_alpha = alphas[optimal_idx]
    return optimal_alpha

if __name__ == '__main__':

    up_one_dir = '../'
    amfAR_fp = up_one_dir + 'data/amfAR/countydata.tsv'
    msm_fp = up_one_dir + "data/CAMP/US_MSM_Estimates_Data_2013.csv"
    employment_fp = up_one_dir + "data/ACS_14_5YR_employment/ACS_14_5YR_S2301_with_ann.csv"
    income_fp = up_one_dir + "data/ACS_14_5YR_income/ACS_14_5YR_S1901_with_ann.csv"
    poverty_fp = up_one_dir + "data/ACS_14_5YR_poverty/ACS_14_5YR_S1701_with_ann.csv"    

    df = pipe.hiv_data_pipe(amfAR_fp=amfAR_fp, msm_fp=msm_fp, employment_fp=employment_fp, income_fp=income_fp, poverty_fp=poverty_fp)

    cleaned_data = pipe.clean_data(amfAR_fp, msm_fp, employment_fp, income_fp, poverty_fp)

    X, y = pipe.get_X_y(cleaned_data)

    X_train, X_test, y_train, y_test = train_test_split(X, y)

    cv_func = cv(X_train, y_train, n_folds=5, alpha=0.5)
    print(cv_func)

    lasso= Lasso(alpha=0.5)
    lasso.fit(X,y)
    y_hat = lasso.predict(X)
    MSE = rss(y, y_hat)
    print(MSE)

    #without outliers
    no_outliers = cleaned_data.copy()
    pipe.remove_outliers(no_outliers)
    
    X_2, y_2 = pipe.get_X_y(no_outliers)
    X2_train, X2_test, y2_train, y2_test = train_test_split(X_2, y_2)

    cv_func2 = cv(X2_train, y2_train, n_folds=5, alpha=0.5)

    print(cv_func2)

    lasso2= Lasso(alpha=0.5)
    lasso2.fit(X_2,y_2)
    y_hat2 = lasso2.predict(X_2)
    MSE2 = rss(y_2, y_hat2)
    print(MSE2)

    lasso_coef = lasso.coef_
    print(lasso_coef)
    
    lasso_coef2 = lasso2.coef_
    print(lasso_coef2)

    print(X_2.columns)
    x = ['MSE with Outlier', 'MSE without Outlier']
    fig, ax = plt.subplots(1)
    ax.bar(x, [MSE, MSE2])
    ax.set_ylabel('MSE Value')
    ax.set_title('MSE Comparison with and without Outlier from Scott County, Indiana')
    plt.savefig('../images/mse.png')

    #lasso_alphas = [0.0001, 0.001, 0.01, 0.1, 1, 10]

    #alpha_train = train_at_various_alphas(X, y, lasso_alphas)
    #print(alpha_train)

    # lasso_cv_errors_train, lasso_cv_errors_test = train_at_various_alphas(X_train.values, y_train.values, lasso_alphas, max_iter=100)

    # lasso_mean_cv_errors_train = lasso_cv_errors_train.mean(axis=0)
    # lasso_mean_cv_errors_test = lasso_cv_errors_test.mean(axis=0)

    #optimal_alpha = get_optimal_alpha(mean_cv_errors_test)

    # lasso_optimal_alpha = get_optimal_alpha(lasso_mean_cv_errors_test)

    # lasso_cv_errors_train, lasso_cv_errors_test = train_at_various_alphas(X_train.values, y_train.values, Lasso, lasso_alphas)

    # lasso_mean_cv_errors_train = lasso_cv_errors_train.mean(axis=0)
    # lasso_mean_cv_errors_test = lasso_cv_errors_test.mean(axis=0)

    # lasso_optimal_alpha = get_optimal_alpha(lasso_mean_cv_errors_test)

    # fig, ax = plt.subplots(figsize=(14, 4))
    # ax.plot(np.log10(lasso_alphas), lasso_mean_cv_errors_train)
    # ax.plot(np.log10(lasso_alphas), lasso_mean_cv_errors_test)
    # ax.axvline(np.log10(lasso_optimal_alpha), color='grey')
    # ax.set_title("LASSO Regression Train and Test MSE")
    # ax.set_xlabel(r"$\log(\alpha)$")
    # ax.set_ylabel("MSE")

    # lasso_models = []

    # for alpha in lasso_alphas:
    #     scaler = XyScaler
    #     scaler.fit(X_train.values, y_train.values)
    #     X_train_std, y_train_std = scaler.transform(X_train.values, y_train.values)
    #     lasso = Lasso(alpha=alpha)
    #     lasso.fit(X_train_std, y_train_std)
    #     lasso_models.append(lasso)

    # paths = pd.DataFrame(np.empty(shape=(len(lasso_alphas), len(X_train.columns))),
    #                     index=lasso_alphas, columns=X_train.columns)

    # for idx, model in enumerate(lasso_models):
    #     paths.iloc[idx] = model.coef_
        
    # fig, ax = plt.subplots(figsize=(14, 4))
    # for column in X_train.columns:
    #     path = paths.loc[:, column]
    #     ax.plot(np.log10(lasso_alphas), path, label=column)
    # ax.axvline(np.log10(lasso_optimal_alpha), color='grey')
    # ax.legend(loc='lower right')
    # ax.set_title("LASSO Regression, Standardized Coefficient Paths")
    # ax.set_xlabel(r"$\log(\alpha)$")
    # ax.set_ylabel("Standardized Coefficient")
