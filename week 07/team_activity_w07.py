import random

random_num = random.randint(1,100)
# print(random_num)

input_number = 0
try_again = "y"

while random_num != input_number and try_again == "y":
    input_number = int(input("What is the magic number? "))

    if random_num > input_number:
        
        print("Higher!")
        try_again_bruto = input("Do you want to try again (y/n)?")
        try_again = try_again_bruto.lower()
        if try_again == "n":
            print("\n\nPrograma encerrado pelo user")

    elif random_num < input_number:
        print("Lower!")
        try_again_bruto = input("Do you want to try again (y/n)?")
        try_again = try_again_bruto.lower()
        if try_again == "n":
            print("\n\nPrograma encerrado pelo user")
    else:
        print("\nAcertouuu!🎉🎉✨✨")


