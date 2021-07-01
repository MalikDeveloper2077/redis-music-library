from src.models import Song
from src.views import print_all_objects


def create_song():
    name = input('Your favorite song\n> ')
    duration = input('The song duration\n> ')
    streams = int(input('The song streams\n> '))
    return Song(name, duration, streams)


def main():
    song = create_song()
    Song.db.save(song)
    print_all_objects(
        keys=Song.db.get_all_objects(song)
    )


if __name__ == '__main__':
    main()
