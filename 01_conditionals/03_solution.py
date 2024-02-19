### Grade Calculator: Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D(60-69), F (below 60)

score = int(input("Enter your score: "))

grade = ""

if score > 100 or score < 0:
	print ("Invalid score, Enter score again!")
else:
	if score < 60:
		grade = "F"
	elif score < 70:
		grade = "D"
	elif score < 80:
		grade = "C"
	elif score < 90:
		grade = "B"
	else:
		grade = "A"

	print("Your grade is", grade)

# exit() ## exits program
	
