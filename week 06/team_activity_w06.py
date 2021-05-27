print("Welcome!")
is_able_to_ride = ""
first_rider_age = int(input("What is the age of the first rider? "))
first_rider_height = float(input("What is the height of the first rider? "))

is_a_second_rider = input("Is there a second rider (yes/no)? ")


if is_a_second_rider == "yes":
    second_rider_age = int(input("What is the age of the second rider? "))
    second_rider_height = float(input("What is the height of the second rider? "))

    if first_rider_height >= 36 and second_rider_height >= 36:
        if first_rider_age >= 18 or second_rider_age >= 18:
            is_able_to_ride = True
        else:
            is_able_to_ride = False
    else:
        is_able_to_ride = False


elif is_a_second_rider == "no": 
    if first_rider_age >= 18 and first_rider_height >= 62:
        is_able_to_ride = True
    else:
        is_able_to_ride = False

else:
   print("you should put yes or no")

if is_able_to_ride:
    print("You can ride!")
elif is_able_to_ride == False:
    print("You can't ride!")
