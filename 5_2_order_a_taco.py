# 5.2 Order a taco 

# SET UP
veggies = ["chili-fried tofu", "spicy tempeh", "refried beans"]
meats = ["ground beef", "pork carnitas", "spicy chicken"]
toppings = ["radishes", "pickled onion", "cilantro"]

print("Place your taco order:")

# INPUT / PROCESSING
# choose a tortilla
tortilla = input("\nWould you like a corn or flour tortilla?: ")

# vegetarian?
vegetarian = input("\nAre you vegetarian? (y/n): ")

# choose a protein
if vegetarian == "n":
    print("\tChoose 1 for", meats[0],
          "\n\tChoose 2 for", meats[1],
          "\n\tChoose 3 for", meats[2])
    meat_index = int(input("\nWhich protein would you like?: ")) - 1
    protein = meats[meat_index]
else:
    print("\tChoose 1 for", veggies[0],
          "\n\tChoose 2 for", veggies[1],
          "\n\tChoose 3 for", veggies[2])
    veggie_index = int(input("\nWhich protein would you like?: ")) - 1
    protein = veggies[veggie_index]

# choose a topping
print("\nNow choose a topping:",
      "\n\tChoose 1 for", toppings[0],
      "\n\tChoose 2 for", toppings[1],
      "\n\tChoose 3 for", toppings[2])
toppings_index = int(input("\nWhich toppings would you like?: ")) - 1
topping = toppings[toppings_index]

# salsa?
salsa = input("\nWould you like spicy salsa on that? (y/n): ")
if salsa == "y":
    salsa = "spicy salsa"
else:
    salsa = "no spicy salsa"

# OUTPUT
# display taco order
print(f"\nOK, that's one {protein} taco on a {tortilla} tortilla with {topping} and {salsa}.")
