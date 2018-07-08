from movie import Movie
from user import User

user = User("Vassily")
print(user)
my_movie = Movie("The Matrix", "action", True)
user.movies.append(my_movie)

print(f"User movies: {user.movies}")
print(f"User watched: {user.watched_movies()}")
