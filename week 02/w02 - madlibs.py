# Author: Bruno Belarmino
#
print("\n\n#### Welcome to Python Mad Libs Game ####")
print("\nTo play, please enter the following information:")
print("\n")
adjective = input("adjective: ")
animal = input("animal: ")
verb1 = input("verb: ")
exclamation = input("exclamation: ").capitalize()
verb2 = input("verb: ")
verb3 = input("verb: ")

print("\n")
print("Thank you for these informations :D \n")
print("Your story is:\n\n")
print("The other day, I was really in trouble. It all started when I saw a very "+adjective+" "+animal+" "+verb1+" down the hallway. "+'"'+exclamation+'!"' +
      " I yelled. But all I could think to do was to "+verb2+" over and over. Miraculously, that caused it to stop, but not before it tried to "+verb3+" right in front of my family.")
