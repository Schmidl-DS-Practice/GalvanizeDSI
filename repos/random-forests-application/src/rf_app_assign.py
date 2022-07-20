import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

def convert_yn_bool(x):
    if x == 'yes':
        return True
    else:
        return False


def convert_str_bool(x):
    if x == 'True.':
        return True
    else:
        return False


def clean_df(df):
    columns = ['Phone', 'State']
    df.drop(columns, axis=1, inplace=True)

    df["Int'l Plan"] = df["Int'l Plan"].apply(convert_yn_bool)
    df['VMail Plan'] = df['VMail Plan'].apply(convert_yn_bool)

    df["Churn?"] = df["Churn?"].apply(convert_str_bool)
    y = np.array(df['Churn?'])
    X = np.array(df.drop('Churn?', axis=1))
    return X,y

def importances_df(df,lst):
    df2 = pd.DataFrame()
    df2["Importances"] = lst
    df2["features"] = df.drop('Churn?',axis=1).columns
    return df2

if __name__ == '__main__':
    df = pd.read_csv('data/churn.csv')
    X, y = clean_df(df)
    X_train, X_test, y_train, y_test = train_test_split(X, y)
    rfc = RandomForestClassifier()
    rfc.fit(X_train,y_train)
    pred = rfc.predict(X_test)
    print(confusion_matrix(y_test, pred))
    print('recall', round(recall_score(y_test,pred),3))
    print("precision", round(precision_score(y_test,pred),3))
    print('acc', round(accuracy_score(y_test,pred),3))
    rf = RandomForestClassifier(oob_score=True)
    rf.fit(X_train,y_train)
    importances = rf.feature_importances_
    pred_2 = rf.predict(X_test)
    print('########################')
    print(importances_df(df,importances))
    print(confusion_matrix(y_test, pred_2))
    print('oob', rf.oob_score_)
    print('recall', round(recall_score(y_test,pred_2),3))
    print("precision", round(precision_score(y_test,pred_2),3))
    print('acc oob=true', round(accuracy_score(y_test,pred_2),3))

    acc_list = []
    for n in range(100):
                
        rf_c = RandomForestClassifier(n_estimators=n)
        rfc.fit(X_train,y_train)
        pred = rfc.predict(X_test)
        acc_list.append(accuracy_score(y_test,pred))

    fig, ax = plt.subplots()
    
    


    print(plt.show())




