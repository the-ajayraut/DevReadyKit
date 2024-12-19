#!/bin/bash

# Exit on error
set -e

# Check if inputs are provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <filename> <table_name>"
    exit 1
fi

# Input arguments
FILENAME=$1
TABLE_NAME=$2

# Directory to navigate to
TARGET_DIR="/home/ajay/DevReadyKit/Pyspark/ingest_csv/"

# Virtual environment path
VENV_PATH="/home/ajay/DevReadyKit/Pyspark/venv"

# Python script to run
PYTHON_SCRIPT="ingest_CSV_to_Postgres.py"

# Navigate to the directory
echo "Navigating to $TARGET_DIR..."
cd "$TARGET_DIR"

# Activate virtual environment
echo "Activating virtual environment..."
python3 -m venv "$VENV_PATH"
source "$VENV_PATH/bin/activate"

# Run the Python script
echo "Running Python script..."
python "$PYTHON_SCRIPT" "$FILENAME" "$TABLE_NAME"

# Deactivate virtual environment
echo "Deactivating virtual environment..."
deactivate

echo "Done!"
