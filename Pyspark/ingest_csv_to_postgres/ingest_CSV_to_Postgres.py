#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys


# In[ ]:


# Check if arguments are passed
if len(sys.argv) > 1:
    filename = sys.argv[1]  # First argument (CSV file)
    tablename = sys.argv[2]  # Second argument (Table name)
else:
    # Default values in case arguments are missing
    filename = "default.csv"
    tablename = "default_table"


# In[20]:


from pyspark.sql import SparkSession


# In[21]:


spark = SparkSession.builder \
    .appName("CSV to Postgres Application") \
    .config("spark.jars", "postgresql-42.7.4.jar") \
    .config("spark.driver.bindAddress", "0.0.0.0") \
    .config("spark.ui.port", "4040") \
    .getOrCreate()


# In[22]:


spark.sparkContext.setLogLevel("ERROR")


# In[6]:


# Input CSV File
input_csv = filename #"Employee_202412151916.csv"    # Replace with your CSV file name
pg_table =  tablename #"pg_table_csv"                  # target table - name


# In[7]:


# Postgres credentials
pg_host = "localhost"
pg_port = 5432
pg_db = "postgres"
pg_username = "postgres"
pg_password = "root"


# In[8]:


# PostgreSQL Connection Details
jdbc_url = "jdbc:postgresql://localhost:5432/postgres"
connection_properties = {
    "user": "postgres",
    "password": "root",
    "driver": "org.postgresql.Driver"
}


# In[9]:


# Step 1: Load CSV File into a DataFrame
csv_df = spark.read.option("inferSchema","true").option("header","true").csv(input_csv)


# In[10]:


# Show the DataFrame for validation (optional)
csv_row_count = csv_df.count()


# In[11]:


# Step 2: Write DataFrame to PostgreSQL Table
csv_df.write.jdbc(
    url=jdbc_url,
    table= pg_table, # Name the target table in postgres
    mode="overwrite",
    properties=connection_properties
)
print(f"Data successfully loaded into {pg_table} table.")


# In[12]:


# test postgres table loaded or not.
pg_table_df = spark.read.jdbc(url=jdbc_url, table=pg_table, properties=connection_properties)


# In[14]:


pg_table_row_count = pg_table_df.count()


# In[15]:


if csv_row_count != pg_table_row_count :
    print("CSV not properly loaded")
else:
    print("CSV Load succeed!!!")

