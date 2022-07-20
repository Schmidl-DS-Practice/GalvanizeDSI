import numpy as np
import pandas as pd


def pre_processing(churn, replace_w_means=False):
    churn_ret = churn.copy()

    #bools to ints
    to_replace = {'luxury_car_user':{True:1,False:0},'phone':{'iPhone':1,'Android':0}}
    churn_ret = churn_ret.replace(to_replace)

    #Percentages were in 0-100, setting to 0-1
    churn_ret[['weekday_pct', 'surge_pct']] *= .01

    #Default NAs: ratings of 5, phone iphone
    na_replace_means = {"avg_rating_by_driver" : churn_ret.avg_rating_by_driver.mean(),
                        "avg_rating_of_driver" : churn_ret.avg_rating_of_driver.mean(),
                        "phone" : 1}
    na_replaces = {"avg_rating_by_driver" : 5,
                    "avg_rating_of_driver" : 5,
                    "phone" : 1}
    if replace_w_means:
        churn_ret = churn_ret.fillna(na_replace_means)
    else:
        churn_ret = churn_ret.fillna(na_replaces)

    #Datetimes
    churn_ret['signup_date'] = pd.to_datetime(churn_ret['signup_date'])
    churn_ret['last_trip_date'] = pd.to_datetime(churn_ret['last_trip_date'])

    #Creating target
    churn_ret['churned'] = (churn_ret['last_trip_date'] < '2014-06-01').astype(int)
    churn_ret = churn_ret.drop('last_trip_date', axis = 1)

    #One hotting the city names
    churn_ret = pd.get_dummies(churn_ret, 'city')
    return churn_ret


def eda_processing(churn):
    churn_ret = churn.copy()
    #drop average surge, signup date
    churn_ret = churn_ret.drop(['avg_surge','signup_date'], axis=1)
    return churn_ret

def main():
    churn = pd.read_csv('../data/churn_train.csv')
    print(pre_processing(churn))

if __name__ == "__main__":
    main()