
foods = list()
novo_produto = ""

while novo_produto != "quit":
    novo_produto = input("Please enter the items of the shopping list (type: quit to finish):").lower()

    if novo_produto != "quit":
        foods.append(novo_produto.capitalize())

cont = 0

print()

for food in foods:
    print("Item "+ str(cont) +" - "+ food)
    cont = cont + 1 

item_to_remove = int(input("Which item would you like to change?"))
new_item_to_add = input("What is the new item?")
foods[item_to_remove] = new_item_to_add
print()
cont = 0
for food in foods:
    print("Item "+ str(cont) +" - "+ food)
    cont = cont + 1 