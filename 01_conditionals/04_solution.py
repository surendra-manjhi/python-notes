### Fruit Ripeness Checker
## Problem - Determine if a fruit is ripe, overripe or unripe based on its color. (eg, Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)

fruit = "Banana"
color = input("Enter fruit color: ")

if fruit == "Banana":
	if color == "Green":
		print("Unripe")
	elif color == "Yellow":
		print("Ripe")
	elif color == "Brown":
		print("Overripe")
	else:
		print("Invalid color type!")