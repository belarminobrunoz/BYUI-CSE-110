#https://byui-cse.github.io/cse110-course/lesson09/prepare.html
fruits = list()

while len(fruits) < 4:
    fruits.append(input("Say a neme of a fruit: "))
    #append fruits.append("lemon") adiciona um item à lista
    # print(len(fruits))

for fruit in fruits:
    print(f"-> {fruit}")



