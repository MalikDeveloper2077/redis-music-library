from src.models import Song
from src.redis_client import get_redis_connection
from src.views import print_all_objects


def create_song():
    name = input('Your favorite song\n> ')
    duration = input('The song duration\n> ')
    streams = int(input('The song streams\n> '))
    return Song(name, duration, streams)


def main(redis_connection):
    song = create_song()
    song.db.save(redis_connection, song)
    print_all_objects(
        redis_connection,
        keys=Song.db.get_all_objects(redis_connection, song)
    )


if __name__ == '__main__':
    main(get_redis_connection())
