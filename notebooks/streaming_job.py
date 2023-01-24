# Databricks notebook source
rowsPerSeconds = 50
rampUpTime = 5
numPartitions = 10

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
