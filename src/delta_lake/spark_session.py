from pyspark.sql import SparkSession


def configure_spark_session(cores:int, app_name: str):
    max_cpu = max(1, cores-1)
    spark = SparkSession.builder \
    .appName(app_name) \
    .master(f"local[{max_cpu}]") \
    .config("spark.driver.host", "192.168.1.111") \
    .config("spark.jars.package", "io.delta:delta-core_2.12:1.2.1") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
    .getOrCreate()
    return spark
