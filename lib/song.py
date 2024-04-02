class Song:
    count = 0
    genre_count = {}
    artist_count = {}
    genres = []
    artists = []
    
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        Song.add_song_to_count(self)
        Song.add_to_genres(self)
        Song.add_to_artists(self)
        Song.add_to_genre_count(self)
        Song.add_to_artist_count(self)

    @classmethod
    def add_song_to_count(cls, song):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, song):
        if song.genre not in cls.genres:
            cls.genres.append(song.genre)

    @classmethod
    def add_to_artists(cls, song):
        if song.artist not in cls.artists:
            cls.artists.append(song.artist)

    @classmethod
    def add_to_genre_count(cls, song):
        for genre in cls.genres:
            if genre in cls.genre_count and genre == song.genre:
                cls.genre_count[genre] += 1
            else:
                cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, song):
        for artist in cls.artists:
            if artist in cls.artist_count and artist == song.artist:
                cls.artist_count[artist] += 1
            else:
                cls.artist_count[artist] = 1
