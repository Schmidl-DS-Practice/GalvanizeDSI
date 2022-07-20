import pyspark as ps
import pandas as pd
from scipy import sparse
from pyspark.sql import SparkSession
from pyspark.sql.functions import lit
from pyspark.ml.recommendation import ALS
import numpy as np
import timeit

# Time Test
starttime = timeit.default_timer()

spark = SparkSession.builder.getOrCreate()

ratings_df = pd.read_csv('data/ml-latest-small/ratings.csv')
movies_df = pd.read_csv('data/ml-latest-small/movies.csv')
tags_df = pd.read_csv('data/ml-latest-small/tags.csv')
links_df = pd.read_csv('data/ml-latest-small/links.csv')

ratings_df.drop(columns='timestamp', inplace=True)
# Merge ratings with movies
ratings_movies_merge = ratings_df.merge(movies_df, how='left', on='movieId')

spark_df_ratings_movies = spark.createDataFrame(ratings_movies_merge)

train, test = spark_df_ratings_movies.randomSplit([0.8,0.2], seed=142)

als_model = ALS(itemCol='movieId',
                userCol='userId',
                ratingCol='rating',
                nonnegative=True,
                regParam=0.1,
                rank=10)

recommender = als_model.fit(train)

# one_row_pandas = pd.DataFrame({'userId': [1], 'movieId':[100]})
# one_row_spark = spark.createDataFrame(one_row_pandas)

# predict_one = recommender.transform(one_row_spark)
# predict_one.show()
# items_factor_df = recommender.itemFactors.toPandas()
# user_factor_df = recommender.userFactors.toPandas()
predictions = recommender.transform(test)
# predictions.describe().show()
train_df = train.toPandas()
predictions_df = predictions.toPandas()
predictions_df.fillna(train_df['rating'].mean(), inplace=True)
predictions_df['MSE'] = (predictions_df['rating']-predictions_df['prediction'])**2
predictions_df['RMSE'] = (predictions_df['MSE'])**0.5
RMSE_tot = predictions_df['RMSE'].sum()
RMSE_count = predictions_df['RMSE'].shape[0]
RMSE = RMSE_tot/RMSE_count
print(f'The RMSE is {RMSE:.4f}')
print(predictions_df.describe())

print(f"The time to run the model is {timeit.default_timer() - starttime:.2f}")






