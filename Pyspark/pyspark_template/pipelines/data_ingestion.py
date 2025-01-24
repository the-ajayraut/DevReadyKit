# pipelines/data_ingestion.py

from utils.io_utils import read_csv
from utils.schema_utils import get_customer_schema
from config import INPUT_PATH

def ingest_customer_data(spark):
    """
    Ingest customer data from CSV files.
    """
    schema = get_customer_schema()
    return read_csv(spark, f"{INPUT_PATH}/customers.csv", schema)
