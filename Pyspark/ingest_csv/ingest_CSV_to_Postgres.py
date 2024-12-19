#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys


# In[2]:


# Check if arguments are passed
if len(sys.argv) > 1:
    filename = sys.argv[1]  # First argument (CSV file)
    tablename = sys.argv[2]  # Second argument (Table name)
else:
    # Default values in case arguments are missing
    filename = "Employee_202412151916.csv"
    tablename = "default_csv_table"


# In[3]:


from pyspark.sql import SparkSession


# In[4]:


spark = SparkSession.builder \
    .appName("CSV to Postgres Application") \
    .config("spark.jars", "postgresql-42.7.4.jar") \
    .config("spark.driver.bindAddress", "0.0.0.0") \
    .config("spark.ui.port", "4040") \
    .getOrCreate()


# In[5]:


spark.sparkContext.setLogLevel("ERROR")


# In[10]:


# Input CSV File
input_csv = "/home/ajay/DevReadyKit/Pyspark/ingest_csv/Employee_202412151916.csv" #+ filename  # Replace with your CSV file name
pg_table = "default_csv_table"                 # target table - name


# In[11]:


# Postgres credentials
pg_host = "localhost"
pg_port = 5432
pg_db = "postgres"
pg_username = "postgres"
pg_password = "root"


# In[12]:


# PostgreSQL Connection Details
jdbc_url = "jdbc:postgresql://localhost:5432/postgres"
connection_properties = {
    "user": "postgres",
    "password": "root",
    "driver": "org.postgresql.Driver"
}


# In[13]:


# Step 1: Load CSV File into a DataFrame
csv_df = spark.read.option("inferSchema","true").option("header","true").csv(input_csv)


# In[18]:


#Remove double quotes from column names in when loading CSV
csv_df = csv_df.toDF(*[col.lower() for col in csv_df.columns])      


# In[16]:


# Show the DataFrame for validation (optional)
csv_row_count = csv_df.count()


# In[17]:


# Step 2: Write DataFrame to PostgreSQL Table
csv_df.write.jdbc(
    url=jdbc_url,
    table= pg_table, # Name the target table in postgres
    mode="overwrite",
    properties=connection_properties
)
print(f"Data successfully loaded into {pg_table} table.")


# In[15]:


# test postgres table loaded or not.
pg_table_df = spark.read.jdbc(url=jdbc_url, table=pg_table, properties=connection_properties)


# In[16]:


pg_table_row_count = pg_table_df.count()


# In[17]:


if csv_row_count != pg_table_row_count :
    print("CSV not properly loaded")
else:
    print("CSV Load succeed!!!")

