from movie import Movie
class User:
    """docstring for User."""
    def __init__(self, name):
        self.name = name
        self.movies = []

    def add_movie(self, name, genre):
        # my_user_object.add_movie(name, genre)
        movie = Movie(name, genre, False)
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

    def json(self):
        return {
            'name': self.name,
            'movies': [
                movie.json() for movie in self.movies
            ]
        }

    @classmethod
    def from_json(cls, jsondata):
        user = User(jsondata['name'])
        movies = []
        for movie_data in jsondata['movies']:
            movies.append(Movie.from_json(movie_data))
        user.movies = movies
        print(user)
        return user






    # def save2csv(self):
    #     fname = f"{self.name}.txt"
    #     with open(fname, 'w') as f:
    #         f.write(self.name + "\n")
    #         for movie in self.movies:
    #             pattern = "{},{},{}\n"
    #             f.write(pattern.format(movie.name, movie.genre, movie.watched))
    #
    # @classmethod
    # def load_csv(cls, fn):
    #     with open(fn, 'r') as f:
    #         content = f.readlines()
    #         username = content[0][:-1]
    #         movies = []
    #         for line in content[1:]:
    #             mdata = line.split(',')
    #             movies.append(Movie(mdata[0], mdata[1], mdata[2]=='True'))
    #         # user = User(username)
    #         user = cls(username)
    #         user.movies = movies
    #         return user
