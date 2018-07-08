from user import User
from movie import Movie

user = User('Vassily')
user.add_movie("The Matrix", "Action")
user.add_movie("The Interview", "Comedy")
user.save2csv()

# BEFORE WRITING TO CSV
# from movie import Movie
# from user import User
#
# user = User("Vassily")
# print(user)
# my_movie = Movie("The Matrix", "action", True)
# user.movies.append(my_movie)
#
# print(f"User movies: {user.movies}")
# print(f"User watched: {user.watched_movies()}")
