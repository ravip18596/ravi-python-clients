import logging
from src.utils.logger import CustomAdapter, fetch_env_logger


def get_trace_logger(trace_id: str):
    new_logger = logging.getLogger(__name__)
    logging.basicConfig(format='%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s.%(funcName)s:%(lineno)d] %(message)s',
                        datefmt='%Y-%m-%d:%H:%M:%S',
                        level=fetch_env_logger())
    new_logger = CustomAdapter(new_logger, {'trace_id': trace_id})

    return new_logger