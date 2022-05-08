from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
from src.utils.logger import logger
from src.utils.cores import get_max_cores
from src.delta_lake.spark_session import configure_spark_session
from typing import List, Tuple

spark = configure_spark_session(get_max_cores())

class DeltaLakeSpark:
    def __init__(self, spark_session: SparkSession = None):
        """
        using spark sql
        """
        if spark_session is None:
            self.spark = spark
        else:
            self.spark = spark_session


    def create_database(database_name: str):
        create_db_query = f"CREATE DATABASE {database_name}"
        try:
            self.spark.sql(create_db_query)
            logger.info(f"{database_name} is created")
        except Exception as e:
            logger.exception(f"Exception: {str(e)}")

    def create_table_with_schema(
        self,\
         db, table: str,
         schema: List[Tuple], \
         partition_cols: List[str]):

         ddl_sql = f"CREATE TABLE {db}.{table} ("

         for i, col_nanme, col_type in enumerate(schema):
             if i == len(schema)-1:
                 ddl_sql += f"{col_nanme} {col_type}"
             else:
                 ddl_sql += f"{col_nanme} {col_type},"

         ddl_sql += ") USING DELTA "
         if len(partition_cols) > 0:
             ddl_sql += f"[PARTITIONED BY ({','.join(partition_cols)})]"
         try:
             self.spark.sql(ddl_sql)
         except Exception as e:
             logger.exception(f"Exception: {str(e)}")

    def insert(self, table: str, values: List[Tuple]):
         insert_query = f"INSERT INTO {table} values ("
         for value in values:
             insert_query += "(" + ",".join(value) + ")"
         insert_query += ")"
         try:
             self.spark.sql(insert_query)
         except Exception as e:
             logger.exception(f"Exception: {str(e)}")

    def update(self):
        pass
