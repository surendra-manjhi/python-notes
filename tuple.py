# Tuple is as same as List but tuple is immutable.

# Syntax -> keys = (1, 2, 3)

movie_genre = ("horror", "action", "documentary")

# print(movie_genre)
# print(movie_genre[0])
# print(movie_genre[0:])

# movie_genre[0] = "comedy" # throw error, as tuple is immutable. References can be changed but actual list can't be mutate.

# print(len(movie_genre))

more = ("comedy", "sci-fi")

all_movie_genre = movie_genre + more

# print(all_movie_genre)

if "comedy" in more:
	print("yess")

# count() # returns count
	
(com, sci) = more # unpacking of tuple

print(com, sci)

print(type(more))

# ("", (), True)