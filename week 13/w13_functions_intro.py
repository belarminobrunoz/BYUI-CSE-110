# INTRODUCTION: https://byui-cse.github.io/cse110-course/lesson13/prepare.html

import datetime

def print_date():
    print("Task Completed")
    print(datetime.datetime.now())
    print()

def get_inicials(name):
    inicials = name[0:1].upper()
    return inicials

first_name = input("Whats your name? ")
print_date()
first_name_initials = get_inicials(first_name)

last_name = input("Whats your last name? ")
print_date()
last_name_initials = get_inicials(last_name)


for x in range(1,10):
    print(x)

print_date()

print(f"Hi {first_name} {last_name}! \
    Your inicials are {first_name_initials}{last_name_initials}")