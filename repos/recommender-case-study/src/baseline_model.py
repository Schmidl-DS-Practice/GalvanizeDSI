import pyspark as ps
import pandas as pd
import numpy as np
from scipy import sparse
from sklearn.model_selection import train_test_split
from surprise import AlgoBase, Dataset, Reader, SVD, SVDpp
from baselines import MeanofMeans
from surprise.model_selection.validation import cross_validate
from collections import defaultdict
import itertools

ratings_df = pd.read_csv('data/ml-latest-small/ratings.csv')
movies_df = pd.read_csv('data/ml-latest-small/movies.csv')
tags_df = pd.read_csv('data/ml-latest-small/tags.csv')
links_df = pd.read_csv('data/ml-latest-small/links.csv')

# Merge ratings with movies
ratings_movies_merge = ratings_df.merge(movies_df, how='left', on='movieId')
df = ratings_movies_merge
train, test = train_test_split(df)
reader = Reader(rating_scale=(1, 5))
train_ds = Dataset.load_from_df(train[['userId', 'title', 'rating']], reader)
test_ds = Dataset.load_from_df(test[['userId', 'title', 'rating']], reader)

train_set = train_ds.build_full_trainset()
missings = train_set.build_anti_testset()
test_set = test_ds.build_full_trainset()
algo_svd = SVD()
algo_mom = MeanofMeans()
algo_svdpp = SVDpp()
cross_validate(algo_mom, train_ds, verbose=True, cv=3)
cross_validate(algo_svd, train_ds, verbose=True, cv=3)
cross_validate(algo_svdpp, train_ds, verbose=True, cv=3)
# algo_svd.fit(train_set)
# predictions = algo_svd.test(missings)

# def top_n_recommendations(predictions, n=5):
#     top_n = defaultdict(list)
#     for uid, iid, true_r, est, _ in predictions:
#         top_n[uid].append((iid, est))

#     for uid, user_ratings in top_n.items():
#             user_ratings.sort(key=lambda x: x[1], reverse=True)
#             top_n[uid] = user_ratings[:n]
#     return top_n

# import itertools
# recs = top_n_recommendations(predictions).items()
# first_10_users = itertools.islice(recs, 10)
# for uid, user_ratings in first_10_users:
#     print(f'User ID: {uid}, Recs: {[iid for (iid, _) in user_ratings]}')


# cross_validate(algo_svd, train_ds, verbose=True, cv=3)
# cross_validate(algo_svdpp, train_ds, verbose=True, cv=3)

# Evaluating RMSE, MAE of algorithm MeanofMeans on 5 split(s).

#                   Fold 1  Fold 2  Fold 3  Fold 4  Fold 5  Mean    Std     
# RMSE (testset)    0.9297  0.9280  0.9320  0.9288  0.9351  0.9307  0.0026  
# MAE (testset)     0.7315  0.7296  0.7338  0.7305  0.7347  0.7320  0.0019  
# Fit time          0.87    0.90    0.92    0.91    0.88    0.90    0.02    
# Test time         0.54    0.53    0.54    0.51    0.52    0.53    0.01    
# Evaluating RMSE, MAE of algorithm SVD on 5 split(s).

#                   Fold 1  Fold 2  Fold 3  Fold 4  Fold 5  Mean    Std     
# RMSE (testset)    0.8863  0.8704  0.8729  0.8643  0.8776  0.8743  0.0074  
# MAE (testset)     0.6788  0.6670  0.6717  0.6643  0.6734  0.6711  0.0051  
# Fit time          4.24    4.25    4.32    4.26    4.34    4.28    0.04    
# Test time         0.25    0.25    0.25    0.24    0.20    0.24    0.02


###USE THIIIS

# Evaluating RMSE, MAE of algorithm MeanofMeans on 3 split(s).

#                   Fold 1  Fold 2  Fold 3  Mean    Std     
# RMSE (testset)    0.9339  0.9352  0.9285  0.9325  0.0029  
# MAE (testset)     0.7346  0.7368  0.7281  0.7331  0.0037  
# Fit time          0.52    0.56    0.56    0.55    0.02    
# Test time         0.64    0.64    0.65    0.65    0.00    
# Evaluating RMSE, MAE of algorithm SVD on 3 split(s).

#                   Fold 1  Fold 2  Fold 3  Mean    Std     
# RMSE (testset)    0.8893  0.8904  0.8838  0.8879  0.0029  
# MAE (testset)     0.6824  0.6866  0.6809  0.6833  0.0024  
# Fit time          2.73    2.79    2.83    2.78    0.04    
# Test time         0.31    0.33    0.35    0.33    0.02    
# Evaluating RMSE, MAE of algorithm SVDpp on 3 split(s).

#                   Fold 1  Fold 2  Fold 3  Mean    Std     
# RMSE (testset)    0.8725  0.8784  0.8902  0.8804  0.0073  
# MAE (testset)     0.6689  0.6751  0.6841  0.6760  0.0062  
# Fit time          204.73  201.21  201.97  202.63  1.51    
# Test time         8.21    8.27    8.09    8.19    0.07    
