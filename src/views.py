from typing import Iterable

from src.redis_client import get_value_object


def print_all_objects(keys: Iterable):
    for key in keys:
        print(get_value_object(key))
