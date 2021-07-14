#TASK: https://byui-cse.github.io/cse110-course/lesson13/checkpoint.html

def display_regular(message):
    #display_regular—Receives a string and prints it out, exactly as received.
    print(message)

def display_uppercase(message):
    #display_uppercase—Receives a string, converts it to upper case, and then prints it out.
    print(message.upper())

def display_lowercase(message):
    #display_lowercase—Receives a string, converts it to lower case, and then prints it out.
    print(message.lower())

text = input("Whats is your message? ")
display_lowercase(text)
display_regular(text)
display_uppercase(text)