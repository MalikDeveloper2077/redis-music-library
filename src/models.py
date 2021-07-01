from typing import Union

from src.redis import r
from src.config import song_key_prefix


class Song:
    def __init__(self, name: str, duration: Union[str, int], streams: int):
        self.name = name
        self.duration = duration
        self.streams = streams

    def get_all_data(self):
        return self.__dict__

    def create_redis_song(self):
        for prop in self.get_all_data():
            r.hset(f'{song_key_prefix}-{self.name}', prop, getattr(self, prop))
