import unittest


class MyTestCase(unittest.TestCase):
    def test_logger(self):
        from src.utils.logger import logger
        logger.info("test info log")
        self.assertEqual(True, True)

    def test_trace_logger(self):
        from src.utils.trace_logger import get_trace_logger
        test_trace_id = "1234"
        logger = get_trace_logger(test_trace_id)
        logger.info(f"test info log with trace_id. {test_trace_id}")
        self.assertEqual(True, logger.hasHandlers())


if __name__ == '__main__':
    unittest.main()
