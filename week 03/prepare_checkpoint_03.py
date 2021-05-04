# Write a program that does the following:
## Prompt the user for their age. Convert it to a number, add one to it, and tell them how old they will be on their next birthday.
## Prompt the user for the number of egg cartons they have. Assume each carton holds 12 eggs, multiply their number by 12, and display the total    number of eggs.
## Prompt the user for a number of cookies and a number of people. Then, divide the number of cookies by the number of people to determine how many cookies each person gets.

age_now = int(input("How old are you? "))
age_one_year_after = age_now+1

print("Next year you will be " +str(age_one_year_after))
print("\n----------------")

egg_cartoons = int(input("How much egg cartoons do you have? "))
total_eggs = egg_cartoons*12
print("Nice! So you have "+ str(total_eggs)+" eggs in total!")

print("\n----------------")

cookies = int(input("Give me a number of cookies: "))
people = int(input("Now, give a number of people: "))

num_parts_of_cookies = cookies/people

print(f"If we divide these {cookies} cookies to these {people} people, each person with have {num_parts_of_cookies} parts of cookies")

