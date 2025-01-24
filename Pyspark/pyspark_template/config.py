# config.py

APP_NAME = "IndustryPySparkApp"
MASTER = "local[*]"  # Change to "yarn" for distributed mode
LOG_LEVEL = "INFO"

INPUT_PATH = "./data/input/"
OUTPUT_PATH = "./data/output/"

DEFAULT_PARTITION = 4  # Default number of partitions

