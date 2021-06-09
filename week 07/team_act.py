import random 

answer = "yes"

while answer == "yes":
    number = random.randint(1,100)
    guess = ""

    count = 0

    while guess != number: 
        guess = int(input("What is your guess? "))
        
        #counts everytime the user tries to answer
        count = count + 1

        if guess > number:
            print("Lower!")
        elif guess < number:
            print("Higher!")
        elif guess == number:
            print("You guessed it!")
        else:
            print("Please use whole numbers")

    print(f"You tried to answer {count} time(s)")
    answer = input("Do you want to play again (yes/no)? ")

print("Thanks for playing 🎇")