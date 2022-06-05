from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
from src.utils.logger import logger
from src.utils.cores import get_max_cores
from src.delta_lake.spark_session import configure_spark_session
from typing import List, Tuple

spark = configure_spark_session(cores=get_max_cores(), app_name="delta_client")

def create_database(database_name: str):
    create_db_query = f"CREATE DATABASE IF NOT EXISTS {database_name}"
    try:
        spark.sql(create_db_query)
        logger.info(f"{database_name} is created")
    except Exception as e:
        logger.exception(f"Exception: {str(e)}")

def create_table_with_schema(
     db, table: str,
     schema: List[Tuple], \
     partition_cols: List[str]):

     ddl_sql = f"CREATE TABLE {db}.{table} ("

     i = 0
     for col_name, col_type in schema:
         if i == len(schema)-1:
             ddl_sql += f"{col_name} {col_type}"
         else:
             ddl_sql += f"{col_name} {col_type},"
         i += 1

     ddl_sql += ") USING DELTA "
     if len(partition_cols) > 0:
         ddl_sql += f"PARTITIONED BY ({','.join(partition_cols)});"
     try:
         spark.sql(ddl_sql)
     except Exception as e:
         logger.exception(f"Exception: {str(e)}")

def insert(table: str, values: List[Tuple]):
     insert_query = f"INSERT INTO {table} values ("
     for value in values:
         insert_query += "(" + ",".join(value) + ")"
     insert_query += ");"
     try:
         spark.sql(insert_query)
     except Exception as e:
         logger.exception(f"Exception: {str(e)}")

def read():
    pass

def delete_database(database_name: str):
    drop_db_query = f"DROP DATABASE IF EXISTS {database_name}"
    try:
        spark.sql(drop_db_query)
        logger.info(f"{database_name} is created")
    except Exception as e:
        logger.exception(f"Exception: {str(e)}")

if __name__ == '__main__':
    #delete_database("food_db")
    create_database("food_db")
    create_table_with_schema("food_db", "indian_food",
       [("food_type", "STRING"), ("name", "STRING"), ("price", "FLOAT")], ["food_type"])
