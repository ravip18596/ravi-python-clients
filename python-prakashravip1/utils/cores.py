import os

def get_max_cores() -> int:
    return os.cpu_count()
