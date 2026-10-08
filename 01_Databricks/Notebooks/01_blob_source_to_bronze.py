# Databricks notebook source
# Read CSV files using Auto Loader
df = (spark.readStream
  .format("cloudFiles")
  .option("cloudFiles.format", "csv")
  .option("cloudFiles.schemaLocation", "/Volumes/retail/volumes/blob_source/_schema")
  .option("header", "true")
  .option("inferSchema", "true")
  .load("/Volumes/retail/volumes/blob_source/transactions/")
)

# Write to bronze table - process available data and stop
query = (df.writeStream
  .option("checkpointLocation", "/Volumes/retail/volumes/blob_source/_checkpoint")
  .trigger(availableNow=True)
  .toTable("retail.blob_bronze.transactions")
)

# Wait for the batch to complete
query.awaitTermination()

# COMMAND ----------

# MAGIC %sql
# MAGIC select count(*) from retail.blob_bronze.transactions