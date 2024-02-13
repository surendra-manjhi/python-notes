# List contains one or more elements. List is also known as Array but python community prefers list.

# Syntax-

friends = ["ractor", "vishaal", "aditya", "noorbay", "rupa"]

# print(friends)
# print(friends[0])
# print(friends[-1])

# print(friends[1:4]) # slicing
# print(friends[::2]) # slicing with popping by 1

# friends[2] = "deepu"

# print(friends)

# friends[1:2] = "deepu" # deepu str is treated as array
friends[1:2] = ["supraa"]

# print(friends)

# print(friends[1:1]) # returns empty list

friends[1:1] = ["shww"] # no ele is remove in this way

# print(friends)

# friends[1:3] = []

# print(friends)

# for friend in friends:
# 	print(friend, end="-")


if "deepu" in friends:
	print("gotcha")

friends.append("deepu")

if "deepu" in friends:
	print("gotcha")

# pop() # removes last ele & returns removed ele array
# remove("deepu") # removes ele of your choice & nothing returns
# insert(1, "shivan") # insert ele in list with indecing
# copy() # creates new reference & assign it to var
	
squared_num = [x**2 for x in range(10)] # list comprehension method

print(squared_num)