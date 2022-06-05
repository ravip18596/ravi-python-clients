# ravi-python-clients

Assortment of python client for personal or business use

## Current Facilities

1) Logger with unique identifier per session

## Windows Installation

```commandline
py -m venv venv
source venv\Scripts\activate
py -m pip install python-prakashravip1
```

## Linux/ Mac Installation

```bash
python -m venv venv
source venv/bin/activate
pip install python-prakashravip1
```

## Example

```python
from utils.logger import logger

logger.info("test info log")
```

```python
from utils.trace_logger import get_trace_logger

test_trace_id = "1234"
logger = get_trace_logger(test_trace_id)
logger.info(f"test info log with trace_id. {test_trace_id}")        
```
