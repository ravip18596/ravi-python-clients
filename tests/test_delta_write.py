import unittest
from src.delta_lake.delta_lake_spark import create_database, delete_database

class SparkDeltaWrite(unittest.TestCase):
    def setUp(self):
        self.DATABASE_NAME = "food_db"
    def create_database(self):
        create_database(self.DATABASE_NAME)
    def delete_database(self):
        delete_database(self.DATABASE_NAME)


if __name__ == '__main__':
    unittest.main()
