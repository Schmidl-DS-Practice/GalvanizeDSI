${SPARK_HOME}/bin/spark-submit \
--conf spark.sql.warehouse.dir="file:///tmp/spark-warehouse" \
--master local[4] \
--executor-memory 1G \
--driver-memory 1G \
--packages com.databricks:spark-csv_2.11:1.5.0 \
--packages com.amazonaws:aws-java-sdk-pom:1.10.34 \
--packages org.apache.hadoop:hadoop-aws:2.7.3 \
$1
