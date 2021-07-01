from src import config
from src.config import r
from src.models import Song
from src.views import print_all_songs


"""✅ CONTROLLER ✅"""


def create_redis_song(song: Song):
    for prop in song.get_all_data():
        r.hset(f'{config.song_key_prefix}-{song.name}', prop, getattr(song, prop))


def create_song():
    name = input('Your favorite song\n> ')
    duration = input('The song duration\n> ')
    streams = int(input('The song streams\n> '))
    return Song(name, duration, streams)


def main():
    create_redis_song(create_song())
    print_all_songs()


if __name__ == '__main__':
    main()
