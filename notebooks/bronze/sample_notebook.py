# Databricks notebook source
# MAGIC %md
# MAGIC # Sample Bronze Layer Notebook
# MAGIC This notebook shows how to use the common Python package modules.

# COMMAND ----------

# Import libraries

# Import from the common Python package
from common.utils.logging import error, info

# COMMAND ----------

# MAGIC %md
# MAGIC ## Get parameters

# COMMAND ----------

# Get parameters from the notebook context
dbutils.widgets.text("env", "dev", "Environment")
env = dbutils.widgets.get("env")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Main process

# COMMAND ----------


def main():
    """
    Main execution function.
    """
    try:
        info(f"Starting sample notebook in {env} environment")

        # Your bronze layer data processing code here

        # Example of creating a dataframe
        data = [("John", 25), ("Jane", 30), ("Bob", 40)]
        columns = ["name", "age"]
        df = spark.createDataFrame(data, columns)

        # Display the dataframe
        display(df)

        # Example of processing
        df_filtered = df.filter(df.age > 25)
        display(df_filtered)

        info("Sample notebook execution completed successfully")

    except Exception as e:
        error(f"Error in sample notebook: {str(e)}")
        raise


# COMMAND ----------

# Execute the main function
main()
