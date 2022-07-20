import pyspark as ps

class SparkSession:

    def __init__(self, appname):

        self.appname = appname

    def create_dataframe(self, filename):

        spark = (ps.sql.SparkSession.builder.master("local[4]").appName(self.appname).getOrCreate())
        sc = spark.sparkContext

        le_prez_tweets = self.sc.textFile(filename)

        df = self.spark.read.json(le_prez_tweets)

        return spark, df