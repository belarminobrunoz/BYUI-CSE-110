name = input("What's your name? ")
age = int(input("How old are you? "))
country = input("Where are from? ")

print(f"{name} is {age} years old")

if age >= 18:
    print('You are responsible for yourself')
else:
    print('Your are not responsible for yourself')

if country.capitalize() == 'Brazil':
    print("You're Brazillian!")
else:
    print(f"You are from {country}")
