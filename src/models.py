from typing import Union


"""✅ MODELS ✅"""


class Song:
    def __init__(self, name: str, duration: Union[str, int], streams: int):
        self.name = name
        self.duration = duration
        self.streams = streams

    def get_all_data(self):
        return self.__dict__
