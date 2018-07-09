

# IMPORT FROM JSON
# from user import User
# import json
#
# with open('jsondump.txt', 'r') as f:
#     jsondata  = json.load(f)
#     print(f"jsondata: {jsondata}")
#     user = User.from_json(jsondata)
#     print(user.json())


# EXPORT TO JSON
# from user import User
# import json
#
# user = User('Vassily')
# user.add_movie("The Matrix", "Action")
# user.add_movie("The Interview", "Comedy")
# print(user.json())
# with open('jsondump.txt', 'w') as f:
#     json.dump(user.json(), f)

# IMPORT FROM CSV
# from user import User
# user = User.load_csv('Vassily.txt')
# print(user)
# print(user.movies)

# EXPORT TO CSV
# from user import User
# from movie import Movie
#
# user = User('Vassily')
# user.add_movie("The Matrix", "Action")
# user.add_movie("The Interview", "Comedy")
# user.save2csv()

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
