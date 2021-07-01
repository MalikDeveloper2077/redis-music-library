from typing import Iterable

from src.redis_client import get_value_object


def print_all_objects(redis_connection, keys: Iterable):
    for key in keys:
        print(get_value_object(redis_connection, key))
