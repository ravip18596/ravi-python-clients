import os
from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
from src.utils.logger import logger


class DeltaLakePython':
    def __init__(self, spark_session: SparkSession = None):
        """
        pyspark 3.2.1
        hadoop 3.3.1
        delta-spark 1.1.0
        Spark Shell Scala 2.12
        """
        if spark_session is None:
            conf = SparkConf()
            conf.set('spark.jars.package', 'org.apache.hadoop:hadoop-aws:3.3.1,io.delta:delta-core_2.12:1.1.0')
            conf.set('spark.sql.extensions', 'io.delta.sql.DeltaSparkSessionExtension')
            conf.set('spark.sql.catalog.spark_catalog', 'org.apache.spark.sql.delta.catalog.DeltaCatalog')
            sc = SparkContext(conf=conf)
            spark_session = SparkSession(sc).builder.master("local[2]").appName('delta_client').getOrCreate()
            logger.info("pyspark init successful.")
            self.spark = spark_session
        else:
            self.spark = spark_session

    def create_or_replace_table(self, schema, ):
        pass

    def upsert_df(self):
        pass

    def append_df(self):
        pass
