class Movie:
    def __init__(self, name, genre, watched):
        self.name = name
        self.genre = genre
        # self.director = "Wachowski"
        self.watched = watched
    def __repr__(self):
        return f"<Movie {self.name}>"
