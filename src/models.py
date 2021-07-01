from typing import Union

from src.redis_client import r


class IDBManager:
    """Interface for db managers"""

    def save(self, obj: object):
        raise NotImplementedError

    def get_all_objects(self, obj: object):
        raise NotImplementedError


class DBRedisManager(IDBManager):
    """Song db manager based on redis"""

    def save(self, obj: object):
        for prop in obj.__dict__:
            # Set as key "<name of class>-{obj.__str__}"
            r.hset(f'{obj.__class__.__name__}-{obj.__str__()}', prop, getattr(obj, prop))

    def get_all_objects(self, obj: object):
        return r.scan_iter(match=f'{obj.__class__.__name__}*')


class Song:
    db = DBRedisManager()

    def __init__(self, name: str, duration: Union[str, int], streams: int):
        self.name = name
        self.duration = duration
        self.streams = streams

    def __str__(self):
        return self.name
