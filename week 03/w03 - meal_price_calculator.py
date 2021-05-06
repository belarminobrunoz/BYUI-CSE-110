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

print("Thanks for these information!")

#Calculation part
subtotal = round((childs_meal_price * number_children) + (adults_meal_price * number_adults),2)
sales_tax = round((sales_tax_rate/100)*subtotal,2)
total_meal_price = round(subtotal+sales_tax,2)

print("\nHere is your bill: ")
print("***************************************************")
print("\n")
print(f"Subtotal: {subtotal}")
print(f"Sales tax: {sales_tax}")
print(f"Total price of the meal: {total_meal_price}")
print("\n")
print("***************************************************")
payment_amount = float(input("What's the payment amount? "))
change = round(payment_amount - total_meal_price,2)
print("\n")
print(f"Thank you for your payment! Here is your change: {change}")
