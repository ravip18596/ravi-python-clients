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

### Delta Lake Write client

1) Create/Delete Delta Lake Database
```python
from src.delta_lake.delta_lake_spark import create_database, delete_database

DB_NAME = "food_db"

create_database(DB_NAME)
delete_database(DB_NAME)
```

2) Create Delta Lake Table
```python
from src.delta_lake.delta_lake_spark import create_database, create_table_with_schema

DB_NAME = "food_db"
TABLE_NAME = "indian_food"

create_database(DB_NAME)
create_table_with_schema(db=DB_NAME, table=TABLE_NAME,
     schema=[("food_type", "STRING"), ("name", "STRING"), ("price", "FLOAT")],
     partition_cols=["food_type"])
```

### Logging

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
