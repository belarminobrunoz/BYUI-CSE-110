print("\n\n")
print("Welcome to Bruno's Burguer 🍔")
print("*"*30)
print("\n")
customer_name = input("It's a pleasure to attend you! Please, type your name: ")
print(f"{customer_name} is beatiful name!")
print(f"{customer_name}, in order to process your bill, please, answer the following questions:")

print("\n******** CHILDREN *******")
number_children  = int(input("What was the number of children in our restaurant today? "))# (integer)
childs_meal_price = float(input("What was the price of a child's meal? "))

print("\n")

print("\n******** ADULTS *******")
number_adults  = int(input("What was the number of adults in our restaurant today? ")) #(integer)
adults_meal_price = float(input("What was the price of an adult's meal? "))# (floating point)

print("\n")

sales_tax_rate  = float(input("Please inform the sales tax rate: "))# (floating point)

print("\n")

print(f"Thanks for these information {customer_name}!")

#Calculation part
subtotal = round((childs_meal_price * number_children) + (adults_meal_price * number_adults),2)
sales_tax = round((sales_tax_rate/100)*subtotal,2)
total_meal_price = round(subtotal+sales_tax,2)


print("\n\nHere is your bill: \n"+"*"*30)

print("\n")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Sales tax: ${sales_tax:.2f}")
print(f"Total price of the meal: ${total_meal_price:.2f}")
print("\n")

print("*"*30)
payment_amount = float(input("What's the payment amount? "))
change = round(payment_amount - total_meal_price,2)
print("\n")

print(f"Thank you for your payment {customer_name}! Here is your change: ${change:.2f}")
