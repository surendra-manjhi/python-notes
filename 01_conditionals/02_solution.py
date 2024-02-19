### Movie Ticket Pricing: price 18 (age >= 18), price 8 (child), Wednesday special discount of $2

age = int(input("Enter your age: "))
day = "Wednesday"

# 1st way

price = 0

if age >= 18:
	price = 20
else:
	price = 8

# price = 20 if age >= 18 else 8 # 2nd way

if day == "Wednesday":
	price -= 2

print("Ticket price is $" + str(price))