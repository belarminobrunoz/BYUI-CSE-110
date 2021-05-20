grade = int(input("What's your grade percentage? "))

if grade >= 90:
    letter = "A"
elif grade >= 80:
    letter = "B"
elif grade >= 70:
    letter = "C"
elif grade >= 60:
    letter = "D"
elif grade < 60:
    letter = "F"

sign = "" 

last_digit = grade % 10

if last_digit >= 7:
    sign = "+"
elif last_digit < 3:
    sign = "-"

if grade >= 93 or letter == "F":
    sign = ""



print(f"Your letter grade is {letter}{sign}")

if grade >= 70:
    print("CONGRATULATIONS! 😁")
else:
    print("Game over! Keep working hard! You can do it next time! Don't give up!!")