from typing import Union


class IDBManager:
    """Interface for db managers"""

    def save(self, *args, **kwargs):
        raise NotImplementedError

    def get_all_objects(self, *args, **kwargs):
        raise NotImplementedError


class DBRedisManager(IDBManager):
    """Song db manager based on redis"""

    def save(self, redis_connection, obj: object):
        for prop in obj.__dict__:
            # Set as key "<name of class>-{obj.__str__}"
            redis_connection.hset(f'{obj.__class__.__name__}-{obj.__str__()}', prop, getattr(obj, prop))

    def get_all_objects(self, redis_connection, obj: object):
        return redis_connection.scan_iter(match=f'{obj.__class__.__name__}*')


class Song:
    db = DBRedisManager()

    def __init__(self, name: str, duration: Union[str, int], streams: int):
        self.name = name
        self.duration = duration
        self.streams = streams

    def __str__(self):
        return self.name
