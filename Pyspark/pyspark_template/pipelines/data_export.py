# pipelines/data_export.py

from utils.io_utils import write_parquet
from config import OUTPUT_PATH

def export_customer_data(df):
    """
    Exports customer data to Parquet files.
    """
    write_parquet(df, f"{OUTPUT_PATH}/customers_processed/")
