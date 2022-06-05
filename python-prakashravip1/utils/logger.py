import logging
from typing import MutableMapping, Tuple, Any


class CustomAdapter(logging.LoggerAdapter):
    """ logger formatter new dynamic attribute addition """

    def process(self, msg: Any, kwargs: MutableMapping[str, Any]) -> Tuple[Any, MutableMapping[str, Any]]:
        trace_id = kwargs.pop('trace_id', self.extra.get('trace_id'))
        if trace_id is not None:
            return '[trace_id:%s] %s' % (trace_id, msg), kwargs

        return msg, kwargs


def fetch_env_logger():
    import os
    # default level as INFO
    env_log_level = os.getenv('LOGGING_LEVEL', 'INFO')

    if env_log_level == 'INFO':
        logging_level = logging.INFO
    elif env_log_level == 'ERROR':
        logging_level = logging.ERROR
    elif env_log_level == 'DEBUG':
        logging_level = logging.DEBUG
    elif env_log_level == 'WARN':
        logging_level = logging.WARNING
    else:
        logging_level = logging.INFO

    return logging_level


logging.basicConfig(format='%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s.%(funcName)s:%(lineno)d] %(message)s',
                    datefmt='%Y-%m-%d:%H:%M:%S',
                    level=fetch_env_logger())

logger = logging.getLogger(__name__)
logger = CustomAdapter(logger, {'trace_id': None})