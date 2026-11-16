with open("lesson18/messy_grocery_list.txt") as file:
    contents = file.read().split(",")
groceryList = [item.strip() for item in contents]
print(groceryList)