# utils/schema_utils.py

from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType

def get_customer_schema():
    """
    Returns the schema for the customer dataset.
    """
    return StructType([
        StructField("customer_id", StringType(), True),
        StructField("name", StringType(), True),
        StructField("age", IntegerType(), True),
        StructField("balance", FloatType(), True)
    ])
