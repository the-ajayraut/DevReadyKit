# pipelines/data_validation.py

def validate_customer_data(df):
    """
    Validate that required columns are non-null.
    """
    invalid_count = df.filter(df["customer_id"].isNull()).count()

    if invalid_count > 0:
        raise ValueError("Validation failed: 'customer_id' contains null values.")
