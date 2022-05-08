from pyspark.sql import SparkSession


def configure_spark_session(cores):
    max_cpu = max(1, cores-1)
    spark = SparkSession.builder \
    .appName("quickstart") \
    .master(f"local[{max_cpu}]") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
    .getOrCreate()
