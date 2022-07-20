# import necessary libraries
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.ml.tuning import TrainValidationSplit
from pyspark.ml.recommendation import ALS
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.sql.functions import lit
from pyspark.sql.types import StructType, StructField, IntegerType
from pyspark.sql.functions import countDistinct, col

# Setup a SparkSession
spark = SparkSession.builder.getOrCreate()
sc = spark.sparkContext

schema = StructType([
    StructField("user", IntegerType(), True),
    StructField("movie", IntegerType(), True),
    StructField("rating", IntegerType(), True),
    StructField("timestamp", IntegerType(), True)])
print('\n')

# Load in data
spark_df = spark.read.csv('data/u.data',sep='\t', header=False, schema=schema)

# Convert a Pandas DF to a Spark DF
# spark_df = spark.createDataFrame(df) 

# Convert a Spark DF to a Pandas DF
# pandas_df = spark_df.toPandas()

spark_df = spark_df.drop('timestamp')
# print(spark_df.show())

num_users = spark_df.select('user').distinct().count()
num_movies = spark_df.select('movie').distinct().count()
num_rating = spark_df.count()

density = num_rating / (num_users * num_movies)
# print(density)

train, test = spark_df.randomSplit([0.8, 0.2], seed=427471138)

als_model = ALS(
    itemCol='movie',
    userCol='user',
    ratingCol='rating',
    nonnegative=True,    
    regParam=0.1,
    rank=10)

rec = als_model.fit(train)
data = [(1, 100)]
columns = ('user', 'movie')
one_row_spark_df = spark.createDataFrame(data, columns)
# one_row_pandas_df = pd.DataFrame({'user': [1], 'movie': [100]})
user_factor_df = rec.userFactors.filter('id = 1')
item_factor_df = rec.itemFactors.filter('id = 100')

user_factors = user_factor_df.collect()[0]['features']
item_factors = item_factor_df.collect()[0]['features']
user_item = np.dot(user_factors, item_factors)

rec.transform(one_row_spark_df)

recommender.recommendForUserSubset(one_row_spark_df, 10).

predictions = recommender.transform(test)

predictions.describe().show()


train = train.withColumn("imp_rating", lit(1))
train.show(5)

als_model_imp = ALS(userCol='user',
                itemCol='movie',
                ratingCol='imp_rating',
                implicitPrefs=True,
                nonnegative=True,
                regParam=0.1,
                rank=10
               )

recommender_imp = als_model_imp.fit(train)

# Looking at the recommendations for user 1 to compare to what the explicit gave back 
recommender_imp.recommendForUserSubset(one_row_spark_df, 10).collect()

als_model_imp = ALS(userCol='user',
                itemCol='movie',
                ratingCol='rating',
                implicitPrefs=True,
                nonnegative=True,
                regParam=0.1,
                rank=10
               )

recommender_imp = als_model_imp.fit(train)
recommender_imp.recommendForUserSubset(one_row_spark_df, 10).collect()

