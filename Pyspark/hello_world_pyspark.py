from pyspark.sql import SparkSession

# Initialize Spark session with the correct configuration
spark = SparkSession.builder \
    .appName("PySpark Example") \
    .config("spark.driver.bindAddress", "0.0.0.0") \
    .config("spark.ui.port", "4040") \
    .getOrCreate()

# Your PySpark code here

# Example DataFrame operation
data = [("Alice", 34), ("Bob", 45), ("Cathy", 29)]
columns = ["Name", "Age"]
df = spark.createDataFrame(data, columns)
df.show()

# Keep the session alive to access the UI
input("Press Enter to stop the Spark session...")

# # Stop the Spark session
spark.stop()