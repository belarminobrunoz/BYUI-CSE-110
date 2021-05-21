#Challenge source: https://byui-cse.github.io/cse110-course/lesson05/prove.html
print("\n")
print("Be welcome to Adventure Game! You choose how the story will end!")
print("\n")

meal = (input("Today is friday and your dinner will be a delicious meal. Your companion says that she is in doubt about two options: PIZZA and BURGUER. Which one you choose?\n")).upper()


if meal == "PIZZA": #first level
    print("Yummy! Pizza!")
    flavor = (input("\nOnce you will order pizza, which flavor will you choose? In the menu there is three options: PEPPERONI, CHOCOLATE, HAWAIANA\n")).upper()

    if flavor == "PEPPERONI": #second level
        print("Peperoni is a nice choice!")
        second_flavor = (input("\nThey found out that this is your first order! They want to make you welcome by offering another pizza for free!! There are two flavors:  CHOCOLATE and HAWAIANA. Which flavor will you choose?\n")).upper()

        if second_flavor == "CHOCOLATE": #third level
            print("CHOCOLATE is wonderful!")
        elif second_flavor == "HAWAIANA": #third level
            print("HAWAIANA is gorgeous!")
        else: #third level
            print(f"This flavor {second_flavor} is not include in this offer")       

    elif flavor == "CHOCOLATE": #second level
        print("CHOCOLATE is a sweeeeeet choice!")
        second_flavor = (input("\nThey found out that this is your first order! They want to make you welcome by offering another pizza for free!! There are two flavors:  PEPPERONI and HAWAIANA. Which flavor will you choose?\n")).upper() 

        if second_flavor == "PEPPERONI": #third level
            print("PEPERONI is wonderful!")
        elif second_flavor == "HAWAIANA": #third level
            print("HAWAIANA is gorgeous!")
        else: #third level
            print(f"This flavor {second_flavor} is not include in this offer")

    elif flavor == "HAWAIANA": #second level
        print("So you like salty and sweet together, right? Perfect choice!")
        second_flavor = (input("\nThey found out that this is your first order! They want to make you welcome by offering another pizza for free!! There are two flavors:  PEPPERONI and CHOCOLATE. Which flavor will you choose?\n")).upper()

        if second_flavor == "PEPPERONI": #third level
            print("PEPERONI is wonderful!")
        elif second_flavor == "CHOCOLATE": #third level
            print("CHOCOLATE is AMAZING!")
        else: #third level
            print(f"This flavor {second_flavor} is not include in this offer")

    else: #second level
        print(f"The {flavor} is not on the menu :(")


elif meal == "BURGUER": #first level
    print("\nwohoo! Burguers!!")
    soda = (input("\nOnce you will order burguers, which soda will you choose? In the menu there is two options: COKE or DOLLY\n")).upper()

    if soda == "COKE": #second level
        print("Coke rules!!")
        sauce = (input("\nDo you want a sauce? They have BARBEQUE and MUSTARD. Which one you choose?\n")).upper()
        if sauce == "BARBEQUE": #third level
            print("Barbeque matches very well with burguers!")
        elif sauce == "MUSTARD": #third level
            print("Mustard must be in every burguer in the world!")
        else: #third level
            print("You should choose one of these options: BARBEQUE or MUSTARD")

    elif soda == "DOLLY": #second level
        print("Nice choice! It's the best soda of Brazil!")
        desert = (input("\nOnce you chose a Brazillian drink, why not choose a Brazillian desert? There is two options available: PUDIM or ACAI. Which one you prefer?\n")).upper()

        if desert == "PUDIM": #third level
            print("Pudim is better than Quindim! Nice choice!")
        elif desert == "ACAI": #third level
            print("Acai is heavenly desert! Nice choice!")
        else: #third level
            print(f"This choice {desert} is not acceptable")
    else: #second level
        print("You should choose one of these two options: COKE or DOLLY")

else: #first level
    print(f"Ooops! You should choose between PIZZA and BURGUER. {meal} is not an option.")




if meal == "PIZZA":
    print(f"\n-----------------------------\nYour order will be two Pizzas: \n- A pizza of {flavor.capitalize()}\n- A free pizza of {second_flavor.capitalize()}\n-----------------------------")
elif meal == "BURGUER":
    if soda == "DOLLY":
        print(f"\n-----------------------------\nYour order will be a combo: \n- A burger\n- A {soda.capitalize()} to drink\n- {desert.capitalize()} as a desert.\n-----------------------------")
    elif soda == "COKE":
        print(f"\n-----------------------------\nYour order will be a combo: \n- A burger\n- A {soda.capitalize()} to drink\n- {sauce.capitalize()}'s sauce.\n-----------------------------")
else:
    print("You should choose a meal!")