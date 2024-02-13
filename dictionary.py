user = {"username": "manjhss", "display_name": "Surendra", "age": 20, "is_free": False}

# print(user["username"])
# print(user.get("display_name"))

user["is_free"] = True

# print(user)

# for prop in user:
# 	print(prop, user[prop]) # by default, prop will return keys

for key, value in user.items():
	print(key, ":", value)

if "username" in user:
	print("yess")
 
# print(len(user))

user["loves"] = "programming"

# print(user)

user.pop("is_free") # removes item based on key

# print(user)

user.popitem() # removes last item

del user["age"]

user_copy = user.copy()

# print(user_copy)

# {key: {}, key: {}}

movie_genre = {"action": {"new": "loki", "old": "scarlett"}, "horror": {"new": "wrong turn", "old": "nun"}}

# print(movie_genre)
# print(movie_genre["action"])
# print(movie_genre["action"]["new"])

squared_num = {x: x**2 for x in range(10)}

# print(squared_num)

squared_num.clear() # clear dict ele

# print(squared_num)

keys = ["id", "title", "description"]
default_value = "demo"

new_dict = dict.fromkeys(keys, default_value) # creates dict based on keys and values param

print(new_dict)