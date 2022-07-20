import pyspark as ps
spark = (ps.sql.SparkSession.builder.master("local[4]").appName("sparkSQL_exercise").getOrCreate())
sc = spark.sparkContext

df = spark.read.json('./data/yelp_academic_dataset_business.json.gz')
#df.show()
#df.printSchema()

df.createOrReplaceTempView('yelp_business')

#result = spark.sql("SELECT name, categories, city, state, stars FROM yelp_business LIMIT 10")
#result.show()

#print(df.first())

step_3 = spark.sql("""SELECT DISTINCT name
                      FROM yelp_business
                      LATERAL VIEW explode(categories) c AS category
                      WHERE stars = 5 
                      AND city = 'Phoenix'
                      AND attributes.`Accepts Credit Cards` = 'true'
                      AND category = 'Restaurants'""").collect()
#print(step_3)
#step_3.printSchema()

