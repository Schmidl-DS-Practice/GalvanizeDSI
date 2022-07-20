import json
import matplotlib.pyplot as plt
import pyspark as ps
from class_SparkSession import SparkSession

# spark = (ps.sql.SparkSession.builder.master("local[4]").appName("french_prez_tweets").getOrCreate())
# sc = spark.sparkContext

# # with open('../data/french_tweets.json', 'r') as fin:
# #     fin.read()

# le_prez_tweets = sc.textFile('../data/french_tweets.json')

# df = spark.read.json(le_prez_tweets)

#sample = df.sample(0.1)
#print(df.printSchema())

####################search first names####################
#df.createOrReplaceTempView('emmanuel_tweets')
#emmanuel = spark.sql("""SELECT id, text, created_at
#                      FROM emmanuel_tweets
#                      WHERE text LIKE '%emmanuel%'
#                      """)
#print(macron.show(20))
#print(f'emmanuel tweets: {emmanuel.count()}')

# df.createOrReplaceTempView('marine_tweets')
# marine = spark.sql("""SELECT id, text, created_at
#                      FROM marine_tweets
#                      WHERE text LIKE '%marine%'
#                      """)
#print(lepen.show(20))
#print(f'marine tweets: {marine.count()}')

####################search last names####################
# df.createOrReplaceTempView('macron_tweets')
# macron = spark.sql("""SELECT id, text, created_at
#                       FROM macron_tweets
#                       WHERE text LIKE '%macron%'
#                       """)
#print(macron.show(20))
#print(f'macron tweets: {macron.count()}')

# df.createOrReplaceTempView('pen_tweets')
# lepen = spark.sql("""SELECT id, text, created_at
#                      FROM pen_tweets
#                      WHERE text LIKE '%lepen%'
#                      """)
#print(lepen.show(20))
#print(f'lepen tweets: {lepen.count()}')

####################search total tweets####################
# df.createOrReplaceTempView('total_tweets')
# total = spark.sql(""" SELECT id, text, created_at
#                       FROM total_tweets""")
#print(total.show(20))
#print(f'total tweets: {total.count()}')

####################percent of mentions####################
# percent_macron = macron.count() / total.count()
# percent_lepen = lepen.count() / total.count()
# percent_emmanuel = emmanuel.count() / total.count()
# percent_marine = marine.count() / total.count()

#print(f'emmanuel tweets over total tweets: {percent_emmanuel}')
#print(f'marine tweets over total tweets: {percent_marine}')
#print(f'macron tweets over total tweets: {percent_macron}')
#print(f'lepen tweets over total tweets: {percent_lepen}')

####################media mentions####################

def media_mentions(spark, df):

    df.createOrReplaceTempView('media_tweets')
    media = spark.sql("""
                        SELECT lang, COUNT(lang) AS lang_sum
                        FROM media_tweets
                        GROUP BY lang
                        ORDER BY COUNT(lang) DESC
                        LIMIT 20
                    """)
    print(media.show(40))
    #print(media.count())

def main():

    appname = 'french_prez_tweets'
    filename = '../data/french_tweets.json'

    ss = SparkSession(appname=appname)
    spark, df = ss.create_dataframe(filename=filename)

    media_mentions(spark, df)

if __name__ == "__main__":
    main()