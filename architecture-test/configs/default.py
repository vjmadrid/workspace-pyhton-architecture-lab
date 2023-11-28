import os


# Define the names ot the directories
SOURCE_DIRECTORY_NAME = "src"
CONFIG_DIRECTORY_NAME = "configs"
TEST_DIRECTORY_NAME = "tests"
DOC_DIRECTORY_NAME = "docs"
DATA_DIRECTORY_NAME = "data"
REPORT_DIRECTORY_NAME = "reports"
LOG_DIRECTORY_NAME = "logs"
UPLOAD_DIRECTORY_NAME = "uploads"


# Define the application directory path
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Define the application directories path
SOURCE_DIR = os.path.join(BASE_DIR, SOURCE_DIRECTORY_NAME)
CONFIG_DIR = os.path.join(BASE_DIR, CONFIG_DIRECTORY_NAME)
TEST_DIR = os.path.join(BASE_DIR, TEST_DIRECTORY_NAME)
DOC_DIR = os.path.join(BASE_DIR, DOC_DIRECTORY_NAME)
DATA_DIR = os.path.join(BASE_DIR, DATA_DIRECTORY_NAME)
REPORT_DIR = os.path.join(BASE_DIR, REPORT_DIRECTORY_NAME)
LOGS_DIR = os.path.join(BASE_DIR, LOG_DIRECTORY_NAME)
UPLOAD_DIR = os.path.join(BASE_DIR, UPLOAD_DIRECTORY_NAME)
