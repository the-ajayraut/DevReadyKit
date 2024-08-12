# Setting Up PySpark on Ubuntu (Without Docker)

This guide provides detailed steps to set up PySpark on an Ubuntu system running on WSL (Windows Subsystem for Linux). 
It covers updating packages, installing dependencies, setting up Spark, and optionally using a virtual environment for running PySpark.

## Steps to Setup PySpark

### 1. Update Packages

Start by updating your package list to ensure you have the latest information about the available packages:

```bash
sudo apt update
```

###2. Install Python
```commandline
sudo apt install python3 python3-pip
```

###Verify Installation
```commandline
python3 --version
pip3 --version
```

###3. Install Java
```commandline
sudo apt install openjdk-11-jdk
```

###Verify Installation
```commandline
java -version
```

###4. Download and Install Apache Spark
```commandline
wget https://archive.apache.org/dist/spark/spark-3.4.0/spark-3.4.0-bin-hadoop3.tgz
```

###Extract Spark
```commandline
tar xvf spark-3.4.0-bin-hadoop3.tgz
```

###Move Spark to the Desired Directory
```commandline
sudo mv spark-3.4.0-bin-hadoop3 /opt/spark
```

###5. Set Environment Variables
```commandline
export SPARK_HOME=/opt/spark
export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin
export PYSPARK_PYTHON=python3
```

###Apply changes
```commandline
source ~/.bashrc
```

###6. Install PySpark
```commandline
pip3 install pyspark
```

###Optional: Use a Virtual Environment
####Install the Virtual Environment Package
```commandline
sudo apt install python3-venv
```


###7. Create a virtual environment
```commandline
python3 -m venv venv
```

###Activate virtual environment
```commandline
source venv/bin/activate
```

###Install PySpark Inside the Virtual Environment
```commandline
pip install pyspark
```

###Deactivate
```commandline
deactivate
```