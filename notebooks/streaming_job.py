# Databricks notebook source
rowsPerSeconds = 50
rampUpTime = 10
numPartitions = 1

# COMMAND ----------

df = (
    spark.readStream.format("rate")
    .option("rowsPerSecond", rowsPerSeconds)
    .option("rampUpTime", rampUpTime)
    .option("numPartitions", numPartitions)
    .load()
)

# COMMAND ----------

display(df)
