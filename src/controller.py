from src import config
from src.redis import r
from src.models import Song
from src.views import print_all_songs


def create_song():
    name = input('Your favorite song\n> ')
    duration = input('The song duration\n> ')
    streams = int(input('The song streams\n> '))
    return Song(name, duration, streams)


def main():
    create_song().create_redis_song()
    print_all_songs(
        songs=r.scan_iter(match=f'{config.song_key_prefix}*'),
        print_song_function=r.hgetall
    )


if __name__ == '__main__':
    main()
