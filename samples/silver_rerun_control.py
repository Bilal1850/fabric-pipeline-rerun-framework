# Silver-layer rerun control (excerpt).
# Reads the notebook control view and selects notebooks that are Pending or Failed
# for a source system, so they can be re-executed in dependency order
# (sequence_no / parallel_group). Excerpt ends where the original screenshot ends.

import com.microsoft.spark.fabric
from pyspark.sql.functions import col
from pyspark.sql import SparkSession
from notebookutils import mssparkutils
from datetime import datetime, timedelta

spark = SparkSession.builder.getOrCreate()

# -----------------------
# Step 1: Read control table
# -----------------------
control_df = spark.read.synapsesql("DataOpsWarehouse.Metadata.Control_Notebook_Exec_vw").drop("notebook_path")

# -----------------------
# Step 2: Filter Pending + Failed for the source system
# -----------------------
pending_df = control_df.filter(
    ((col("status") == "Pending") | (col("status") == "Failed")) & (col("SourceSystem") == "CBS")
)

# ... (remaining steps: order by sequence_no, run each parallel_group,
#      update NoteBookActivityLog with the new status)
