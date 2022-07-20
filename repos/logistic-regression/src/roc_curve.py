import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, KFold
from sklearn import metrics

def roc_curve(probabilities, labels):
    '''
    INPUT: numpy array, numpy array
    OUTPUT: list, list, list

    Take a numpy array of the predicted probabilities and a numpy array of the
    true labels.
    Return the True Positive Rates, False Positive Rates and Thresholds for the
    ROC curve.
    '''
    df_prob = pd.DataFrame({'probabilities':probabilities, 'label': labels})
    df_prob.sort_values('probabilities', inplace=True)
    thresh_array = []
    fpr_array = []
    tpr_array = []
    for i in df_prob['probabilities']:
        y_hat = np.zeros(len(df_prob))
        tn = 0
        tp = 0
        fp = 0
        fn = 0
        for idx2, j in enumerate(df_prob['probabilities']):
            if j >= i:
                y_hat[idx2] = 1
            else:
                y_hat[idx2] = 0
            if (df_prob['label'][idx2] == y_hat[idx2]) and (y_hat[idx2] == 0):
                tn += 1
            elif (df_prob['label'][idx2] == y_hat[idx2]) and (y_hat[idx2] == 1):
                tp += 1
            elif (df_prob['label'][idx2] != y_hat[idx2]) and (y_hat[idx2] == 1):
                fp += 1
            elif (df_prob['label'][idx2] != y_hat[idx2]) and (y_hat[idx2] == 0):
                fn += 1
        thresh_array.append(i)
        fpr_array.append((fp)/(tn + fp))
        tpr_array.append((tp)/(tp + fn))
    return (tpr_array, fpr_array, thresh_array)

def plot_roc(probabilities, labels):

    tpr, fpr, threshold = roc_curve(probabilities, labels)

    plt.plot(fpr, tpr)
    plt.show()

def cross_val(X_train, y_train):
    kf = KFold(n_splits=5, shuffle=True, random_state=42)
    # print(type(X_train), type(y_train))
    acc_list = []
    prec_list = []
    recall_list = []
    for train_index, test_index in kf.split(X_train):
        X_train_train, X_val = X_train[train_index], X_train[test_index]
        y_train_train, y_val = y_train[train_index], y_train[test_index]
        log = LogisticRegression()
        model = log.fit(X_train_train, y_train_train)
        probs = model.predict_proba(X_val)[:,1]
        #print(probs)
        threshold = 0.5
        y_hat = (probs >= threshold).astype(int)
        accuracy = metrics.accuracy_score(y_val, y_hat)
        precision = metrics.precision_score(y_val, y_hat)
        recall = metrics.recall_score(y_val, y_hat)
        acc_list.append(accuracy)
        prec_list.append(precision)
        recall_list.append(recall)
        # print(accuracy, precision, recall)
        # print(y_hat, y_test)
    mean_acc = np.mean(acc_list)
    mean_prec = np.mean(prec_list)    
    mean_recall = np.mean(recall_list)
    return model

if __name__ == '__main__':
    df = pd.read_csv('../data/grad.csv')
    # print(df.describe())
    rank_df = pd.crosstab(df['admit'], df['rank'])
    # _ = df['gpa'].plot(kind='hist')
    # __ = df['gre'].plot(kind='hist')
    # print(plt.show())
    # print(df.groupby('admit').count())
    
    X = np.array(df.drop('admit', axis=1))
    y = np.array(df['admit'])
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, random_state=56)
    model = (cross_val(X_train, y_train))

    # dummies_df = pd.get_dummies(df, columns=['rank'])
    # X_dum = np.array(dummies_df.drop(['rank_1','admit'], axis=1))
    # y_dum = np.array(dummies_df['admit'])
    # X_train_dum, X_test_dum, y_train_dum, y_test_dum = train_test_split(X_dum, y_dum, train_size=0.8, random_state=56)
    # print(cross_val(X_train_dum, y_train_dum))
    y_hat = model.predict_proba(X_test)[:, 1]
    print(plot_roc(y_hat, y_test))
    