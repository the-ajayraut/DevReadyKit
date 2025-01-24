# main.py

from spark_session import get_spark_session
from pipelines.data_ingestion import ingest_customer_data
from pipelines.data_transformation import enrich_customer_data
from pipelines.data_validation import validate_customer_data
from pipelines.data_export import export_customer_data
from utils.logging_utils import get_logger

def main():
    logger = get_logger("MainApp")
    logger.info("Starting PySpark application...")

    # Initialize SparkSession
    spark = get_spark_session()

    try:
        # Step 1: Data Ingestion
        customer_df = ingest_customer_data(spark)
        logger.info("Data ingestion completed.")

        # Step 2: Data Transformation
        enriched_df = enrich_customer_data(customer_df)
        logger.info("Data transformation completed.")

        # Step 3: Data Validation
        validate_customer_data(enriched_df)
        logger.info("Data validation passed.")

        # Step 4: Data Export
        export_customer_data(enriched_df)
        logger.info("Data export completed.")

    except Exception as e:
        logger.error(f"An error occurred: {e}")
    finally:
        spark.stop()
        logger.info("PySpark application finished.")

if __name__ == "__main__":
    main()
