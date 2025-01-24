# pipelines/data_transformation.py

def enrich_customer_data(df):
    """
    Enriches customer data by adding a new column.
    """
    return df.withColumn("premium_customer", df["balance"] > 10000)
