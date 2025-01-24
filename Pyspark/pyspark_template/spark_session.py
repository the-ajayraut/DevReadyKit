# spark_session.py

from pyspark.sql import SparkSession
from config import APP_NAME, MASTER, LOG_LEVEL

def get_spark_session():
    """
    Creates and configures a SparkSession.
    """
    spark = (
        SparkSession.builder
        .appName(APP_NAME)
        .master(MASTER)
        .config("spark.sql.shuffle.partitions", "200")  # Optimize shuffles
        .getOrCreate()
    )
    spark.sparkContext.setLogLevel(LOG_LEVEL)
    return spark
