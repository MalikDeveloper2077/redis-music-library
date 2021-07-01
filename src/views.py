from src.config import song_key_prefix, r


def print_all_songs():
    for song in r.scan_iter(match=f'{song_key_prefix}*'):
        print(r.hgetall(song))
