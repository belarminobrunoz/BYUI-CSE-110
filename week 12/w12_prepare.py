people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

person_name = ''
person_age = 1000
youngest_person_age = 1000
youngest_person_name = ''


for person in people:
    person_name = person.split()[0]
    person_age = int(person.split()[1])

    print(youngest_person_age, person_age)

    if youngest_person_age > person_age:
        youngest_person_name = person_name
        youngest_person_age =  person_age


print(f"The youngest people on the list is {youngest_person_name} with {youngest_person_age} years old")
        



