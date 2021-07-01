from typing import Union

from src.redis_client import r
from src.config import song_key_prefix


class DbSongManager:
    def save(self, song):
        raise NotImplementedError

    def get_all_songs(self):
        raise NotImplementedError


class SongRedisManager(DbSongManager):
    def save(self, song):
        for prop in song.get_all_data():
            r.hset(f'{song_key_prefix}-{song.name}', prop, getattr(self, prop))

    def get_all_songs(self):
        return r.scan_iter(match=f'{song_key_prefix}*')


class Song:
    db = SongRedisManager()

    def __init__(self, name: str, duration: Union[str, int], streams: int):
        self.name = name
        self.duration = duration
        self.streams = streams

    def get_all_data(self):
        return self.__dict__
