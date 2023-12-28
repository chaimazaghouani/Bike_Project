# Exécution de elasticsearch :
spark-submit \
  --master local[*]\
  --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.4,org.elasticsearch:elasticsearch-spark-30_2.12:8.8.2 \
  --conf "spark.jars.packages=org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.4,org.elasticsearch:elasticsearch-spark-30_2.12:8.8.2" \
  pyspark_consumer_elasticsearch.py > out.txt


# Exécution de hive :
spark-submit \
  --master local[*] \
  --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.4,org.apache.spark:spark-hive_2.12:3.2.4 \
  --conf "spark.jars.packages=org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.4,org.apache.spark:spark-hive_2.12:3.2.4" \
  pyspark_consumer.py > out1.txt

