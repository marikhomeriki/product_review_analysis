import os
import numpy as np

# LOCAL_DATA_PATH = os.path.expanduser(os.environ.get("LOCAL_DATA_PATH"))
# LOCAL_REGISTRY_PATH = os.path.expanduser(os.environ.get("LOCAL_REGISTRY_PATH"))
PROJECT = os.environ.get("PROJECT")
DATASET = os.environ.get("DATASET")
TABLE = os.environ.get("TABLE")


#CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE"))
#DATASET_SIZE = os.environ.get("DATASET_SIZE")
#VALIDATION_DATASET_SIZE = os.environ.get("VALIDATION_DATASET_SIZE")

DTYPES_RAW_OPTIMIZED = {
    "int64_field_0": "int8",
    "string_field_1":"str"
 }
