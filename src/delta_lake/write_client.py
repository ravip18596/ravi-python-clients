import os
from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
from src.utils.logger import logger


class DeltaWriteClient:
    def __init__(
            self,
            bucket: str,
            aws_access_key: str,
            aws_secret_key: str,
            spark_session: SparkSession = None
    ):
        """
        pyspark 3.2.1
        hadoop 3.3.1
        delta-spark 1.1.0
        Spark Shell Scala 2.12
        """
        self.type = type
        self.bucket = bucket
        if spark_session is None:
            os.environ.update({
                'AWS_ACCESS_KEY_ID': aws_access_key,
                'AWS_SECRET_ACCESS_KEY': aws_access_key
            })
            conf = SparkConf()
            conf.set('spark.jars.package', 'org.apache.hadoop:hadoop-aws:3.3.1,' +
                     'com.amazonaws:aws-java-sdk-bundle:1.12.161,' +
                     'io.delta:delta-core_2.12:1.1.0')
            conf.set('spark.sql.extensions', 'io.delta.sql.DeltaSparkSessionExtension')
            conf.set('spark.sql.catalog.spark_catalog', 'org.apache.spark.sql.delta.catalog.DeltaCatalog')
            sc = SparkContext(conf=conf)
            spark_session = SparkSession(sc).builder.master("local[2]").appName('delta_client').getOrCreate()
            spark_session._jsc.hadoopConfiguration().set("fs.s3a.aws.credentials.provider",
                                                         "com.amazonaws.auth.EnvironmentVariableCredentialsProvider")
            spark_session._jsc.hadoopConfiguration().set("fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
            spark_session._jsc.hadoopConfiguration().set("fs.s3a.endpoint", "s3.amazonaws.com")

            logger.info("pyspark init successful.")
            self.spark = spark_session
        else:
            self.spark = spark_session

    def fetch_table_path(self, database: str = "delta_lake", table_name: str = None):
        return f's3a://{self.bucket}/{database}/{table_name}/'

    def create_or_replace_table(self):
        pass

    def upsert_df(self):
        pass

    def append_df(self):
        pass
