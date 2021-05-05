print("\n\n\n")
print("***************************************************")
print("")

childs_meal_price = float(input("The price of a child's meal: "))
adults_meal_price = float(input("The price of an adult's meal: "))# (floating point)
number_children  = int(input("The number of children: "))# (integer)
number_adults  = int(input("The number of adults: ")) #(integer)
sales_tax_rate  = float(input("The sales tax rate: "))# (floating point)


subtotal = (childs_meal_price * number_children) + (adults_meal_price * number_adults)
sales_tax = (sales_tax_rate/100)*subtotal
total_meal_price = subtotal+sales_tax

print("\n\n\n")
print("***************************************************")
print(f"Subtotal: {subtotal}")
print(f"Sales tax: {sales_tax}")
print(f"Total price of the meal: {total_meal_price}")

print("\n\n\n")
print("***************************************************")
payment_amount = float(input("What's the payment amount? "))
change = payment_amount - total_meal_price
print(f"Change: {change}")
