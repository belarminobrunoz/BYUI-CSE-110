#https://byui-cse.github.io/cse110-course/lesson09/prepare.html
fruits = []

while len(fruits) < 4:
    fruits.append(input("Say a name of a fruit: "))


for fruit in fruits:
    print(f"-> {fruit}")

