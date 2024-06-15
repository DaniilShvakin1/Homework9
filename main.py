class MusicAlbum:
    def init(self, title: str, artist: str, release_year: int, genre: str):
        self.title = title
        self.artist = artist
        self.release_year = release_year
        self.genre = genre
        self.songs = []


def get_album_info(self):
    return f"Album: {self.title}\nArtist: {self.artist}\nRelease Year: {self.release_year}\nGenre: {self.genre}"


def add_song(self, song=[]):
    self.songs.append(song)


def remove_song(self, song):
    if song in self.songs:
        self.songs.remove(song)
    else:
        print("Song not found in the album.")


def change_album_info(self, title=None, artist=None):
    if title:
        self.title = title
    if artist:
        self.artist = artist


class MusicColection:
    def init(self, title: str):
        self.title = title
        self.albums = []


def add_album(self, album=[]):
    self.albums.append(album)


def remove_album(self, album=[]):
    if album in self.albums:
        self.albums.remove(album)
    else:
        print("Album not found in the collection.")


def list_albums_info(self):
    for album in self.albums:
        print(album.get_album_info())
    print(f"Total number of albums in collection: {len(self.albums)}")

