# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE CATALOG IF NOT EXISTS retail;
# MAGIC
# MAGIC CREATE SCHEMA IF NOT EXISTS retail.volumes;
# MAGIC CREATE SCHEMA IF NOT EXISTS retail.blob_bronze;
# MAGIC CREATE SCHEMA IF NOT EXISTS retail.postgres_bronze;
# MAGIC CREATE SCHEMA IF NOT EXISTS retail.salesforce_bronze;
# MAGIC
# MAGIC CREATE VOLUME IF NOT EXISTS retail.volumes.blob_source;
# MAGIC
# MAGIC CREATE SCHEMA IF NOT EXISTS retail.retail_silver;
# MAGIC
# MAGIC CREATE SCHEMA IF NOT EXISTS retail.retail_gold;
# MAGIC CREATE SCHEMA IF NOT EXISTS retail.retail_semantic;

# COMMAND ----------

dbutils.fs.mkdirs("/Volumes/retail/volumes/blob_source/transactions")