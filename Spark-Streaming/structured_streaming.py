from pyspark.sql import SparkSession
from pyspark.sql.functions import window, col, sum, avg, current_timestamp

spark = SparkSession.builder \
    .appName("AggregationTable") \
    .config("spark.driver.extraClassPath", "/usr/local/spark-3.3.1-bin-hadoop3/jars") \
    .getOrCreate()
    
jdbc_url = "jdbc:postgresql://postgres:5432/boaz"
jdbc_properties = {
    "user": "boaz",
    "password": "boaz",
    "driver": "org.postgresql.Driver"
}


df = spark.readStream \
    .format("socket") \
    .option("host", "localhost") \
    .option("port", 9999) \
    .load()


data_df = df.selectExpr("CAST(value AS STRING) as json_string") \
    .selectExpr("json_tuple(json_string, 'product_id', 'category_id', 'view_count', 'purchase_count', 'rating') as (product_id, category_id, view_count, purchase_count, rating)")

data_df = data_df.select(
    col("product_id").cast("integer"),
    col("category_id").cast("integer"),
    col("view_count").cast("integer"),
    col("purchase_count").cast("integer"),
    col("rating").cast("float"),current_timestamp().alias("timestamp") 
)

windowed_aggregation = data_df.groupBy(
    window(col("timestamp"), "10 minutes", "5 minutes"), 
    col("category_id")
).agg(
    sum("view_count").alias("total_views"),
    sum("purchase_count").alias("total_purchases"),
    avg("rating").alias("avg_rating")
)

def foreach_batch_function(df, epoch_id):
    df.select(
        col("window.start").alias("window_start"),
        col("window.end").alias("window_end"),
        col("category_id"),
        col("total_views"),
        col("total_purchases"),
        col("avg_rating")
    ).write.jdbc(url=jdbc_url, table="product_table", mode="overwrite", properties=jdbc_properties)
    
    df.show()

query = windowed_aggregation.writeStream \
    .outputMode("complete") \
    .foreachBatch(foreach_batch_function) \
    .start()

query.awaitTermination()
