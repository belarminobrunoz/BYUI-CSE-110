# Main variables 
choice = 0
products_name = list()
products_price = list()

# Here we use a while loop to allow the user to use the menu
while choice != 5:
    # I found out another way to print in multiple lines in this article: https://stackoverflow.com/questions/34980251/how-to-print-multiple-lines-of-text-with-python

    choice = int(input("""
--- Menu --- 

- 1. Add a new item 
- 2. Display the contents of the shopping cart
- 3. Remove an item
- 4. Compute the total
- 5. Quit

Choose a number of the options above: """))

# Based on the menu's choice, the program will enter in a diferent function

    if choice == 1:
        # 1. ADD A NEW ITEM
        print("\n### ADD A NEW ITEM ###\n")
        product = input("Type the name of the item that you would like to add: ")

        # Since we're working with prices, I'll convert to float this input
        price = float(input(f"What is the price of {product}?: "))

        # Here we add the information to the list
        products_name.append(product)
        products_price.append(price)

        print(f"{product} has been added to the cart. ")

    elif choice == 2:

    # 2.DISPLAY THE CONTENTS OF THE SHOPPING CART
       
        print("\n### DISPLAY OF CONTENTS ###\n")
        print("The contents of the shopping cart are: ")

        # I'm using index to calculate a number to display to the users. Lists begins at zero. So, for a better user  visualization, I decided to create this variable index.

        index = 0
        for i in products_name:
            item_number = index + 1
            print(f"{item_number}. {products_name[index]:10} - ${products_price[index]:.2f}")
            index += 1

    elif choice == 3:
    # 3. REMOVE AN ITEM
        print("### REMOVE ITEM ###\n")
        index = 0
        for i in products_name:
            item_number = index + 1
            print(f"{item_number}. {products_name[index]:10} - ${products_price[index]:.2f}")
            index += 1

        print()
        item_to_remove = int(input("Which item would you like to remove? (Type the number of it) "))

        # Here I'm using len to find out how many items we have inside this list
        list_items = len(products_name)

        # This if statement prevents the user to put a number greater than the number of items that is inside of the list 
        if item_to_remove <= list_items:
            index_to_remove = item_to_remove - 1
            
            # Here I'm storing the name of the item before I remove it. This will allow me to print a message with the name of the item that I'll remove.

            products_name_to_remove = products_name[index_to_remove]

            products_name.pop(index_to_remove)
            products_price.pop(index_to_remove)

            print(f"The item {products_name_to_remove} was removed from your shopping cart.")
        else:
            print("Sorry, that is not a valid item number.")

    elif choice == 4:
    # 4. COMPUTE THE TOTAL
        print("### COMPUTE TOTAL ###\n")
        
        total_value = 0
        index = 0

        for value in products_price:
            total_value = total_value + value
            item_number = index + 1
            print(f"{item_number}. {products_name[index]:10} - ${products_price[index]:.2f}")
            index += 1
        print("----------------------")
        print(f"The total price of the items in the shopping cart is ${total_value:.2f}")
        
print("Thanks for using our app! See you!! :D")