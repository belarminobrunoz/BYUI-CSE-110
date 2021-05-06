print("\n\n")
print("Welcome to Bruno's Burguer 🍔")
print("***************************************************")
print("\n")

print("In order to process your bill, please, answer the following questions:")

print("\n******** CHILDREN *******")
number_children  = int(input("What was the number of children? "))# (integer)
childs_meal_price = float(input("What was the price of a child's meal? "))


print("\n******** ADULTS *******")
number_adults  = int(input("What was the number of adults today? ")) #(integer)
adults_meal_price = float(input("What was the price of an adult's meal? "))# (floating point)

print("\n")

sales_tax_rate  = float(input("Please inform the sales tax rate: "))# (floating point)

print("\n")

print("Thanks for the information!")

#Calculation part
subtotal = (childs_meal_price * number_children) + (adults_meal_price * number_adults)
sales_tax = (sales_tax_rate/100)*subtotal
total_meal_price = subtotal+sales_tax

print("\nHere is your bill: ")
print("***************************************************")
print("\n")
print(f"Subtotal: {subtotal}")
print(f"Sales tax: {sales_tax}")
print(f"Total price of the meal: {total_meal_price}")
print("\n")
print("***************************************************")
payment_amount = float(input("What's the payment amount? "))
change = payment_amount - total_meal_price
print("\n")
print(f"Thank you for your payment! Here is your change: {change}")
