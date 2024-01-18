from pyspark.sql import SparkSession
from pyspark.sql.functions import mean, round

spark = SparkSession.builder.master('spark://spark-master:7077').appName("HousePrices").getOrCreate()

db_url = "jdbc:postgresql://db:5432/postgre_db"
con_props = {
    "user": "Evgenii",
    "password": "12345",
    "driver": "org.postgresql.Driver"
}

df = spark.read.jdbc(url=db_url, table="houseprices", properties=con_props)

result_df = df.groupBy("location", "bedrooms") \
    .agg(avg("price").alias("avg_price")) \
    .orderBy("location", "bedrooms")

result_df.show()
