# CSV to PostgreSQL with PySpark

This Pyspark script loads a CSV file into a PostgreSQL table using PySpark.

---

## Files in This Project

- **`ingest_CSV_to_Postgres.ipynb`**: The PySpark script to ingest data from CSV into PostgreSQL.
- **`filename.csv`**: The input CSV file.
- **`postgresql-42.7.4.jar`**: The PostgreSQL JDBC driver required for database connectivity. Download the latest / stable jar for your usecase from [HERE](https://jdbc.postgresql.org/download/)

---

## Setup

1. Place your CSV file in the `ingest_csv` directory and update the `input_csv` variable in `ingest_CSV_to_Postgres.ipynb` with the file name.
2. Update the `pg_table` variable in `Ingest_CSV_to_Postgres.ipynb` with your target PostgreSQL table name.
3. Ensure `postgres.jar` is in the same directory as the script.
4. Following steps are optional, I made these to make my life simpler and run notebook by just providing inputs : filename & tablename
    - Install module to convert notebook to python executable.
    - ``` pip install jupyter nbconvert ```
    - Convert notebook to .py as follows:
    - ``` jupyter nbconvert --to script ingest_csv/ingest_CSV_to_Postgres.ipynb ```
    - Above step will create one more file named same as notebook but with `.py` extension.
    - Execute this `.py` with arguments:
    - ```python ingest_CSV_to_Postgres.py mycsv.csv mycsvtable```