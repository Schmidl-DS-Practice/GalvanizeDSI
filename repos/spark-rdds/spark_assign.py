import pyspark as ps
from spark_intro.py import parse_json_first_key_pair

spark = (ps.sql.SparkSession.builder.master("local[4]").appName("morning sprint").getOrCreate())
sc = spark.sparkContext
lst_rdd = sc.parallelize([1, 2, 3])
file_rdd = sc.textfile('data/cookie_data.txt')

#file_rdd.first()
#file_rdd.take(2)
#file_rdd.collect()
#lst_rdd.collect()

file_rdd_2 = fill_rdd.map(parse_json_first_key_pair)
file_rdd_3 = fill_rdd_2.filter(lambda row: row[1] >= 5)