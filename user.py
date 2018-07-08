class User:
    """docstring for User."""
    def __init__(self, name):
        self.name = name
        self.movies = []

    def add_movie(self, name, genre): # my_user_object.add_movie(name, genre)
        movie = Movie(name, genre)
        self.movies.append(movie)

    def delete_movie(self, name):
        self.movies = list(filter(lambda movie: movie.name!=name, self.movies))



    def watched_movies(self):
        wmovies = list(filter(lambda x: x.watched, self.movies))
        # wmovies = []
        # for m in self.movies:
        #     if m.watched:
        #         wmovies.append(m)
        return wmovies


    def __repr__(self):
        return f"<User {self.name}>"
