number01 = int(input('Insert a number: '))
number02 = int(input('Insert another number: '))

if number01 > number02:
    print(f'The first number ({number01}) is greater than the second ({number02})')
elif number01 < number02:
    print(f'The second number ({number02}) is greater than the first ({number01})')
elif number01 == number02:
    print('Numbers are equal')
elif number01 != number02:
    print('numbers are not equal')


fav_animal = input("Whats your favorite animal? ")
my_fav_animal = "dog"

if fav_animal.lower() == my_fav_animal:
    print(f'No way! I also love {my_fav_animal}!')
else:
    print(f'Nice to know! My favorite animal is {my_fav_animal}')
