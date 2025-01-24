# utils/io_utils.py

def read_csv(spark, path, schema=None):
    """
    Reads a CSV file into a DataFrame.
    """
    return spark.read.csv(path, header=True, schema=schema)

def write_parquet(df, path, mode="overwrite"):
    """
    Writes a DataFrame to a Parquet file.
    """
    df.write.mode(mode).parquet(path)
