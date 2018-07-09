class Movie:
    def __init__(self, name, genre, watched):
        self.name = name
        self.genre = genre
        # self.director = "Wachowski"
        self.watched = watched
    def __repr__(self):
        return f"<Movie {self.name}>"

    def json(self):
        return {
            'name': self.name,
            'genre': self.genre,
            'watched': self.watched
        }

    @classmethod
    def from_json(cls, jsondata):
        return Movie(jsondata['name'], jsondata['genre'], jsondata['watched'])
        # Or, you can do
        # return Movie(**jsondata)
