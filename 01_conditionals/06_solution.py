### Transportation mode selection
## Choose a mode of transportation based on the distance (eg, <3km: walk, 3-15km: bike, >15km: car)

distance = int(input("Enter the distance: "))

mode = ""

if distance < 3:
	mode = "Walk"
elif distance < 16:
	mode = "Bike"
else:
	mode = "Car"

print("Your mode of transportation is", mode)