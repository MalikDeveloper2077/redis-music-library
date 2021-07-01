from typing import Callable


def print_all_songs(songs, print_song_function: Callable):
    for song in songs:
        print(print_song_function(song))
