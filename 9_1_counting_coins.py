# 9.1 Counting coins

import random  # you'll need random for this exercise

# SET-UP

types_of_coins = ["penny", "nickel", "dime", "quarter"]
counted_coins = {}
coins = []

# CREATE A CUP FULL OF CHANGE (create the input)
# randomly create a list of coins to represent your PizzaX cup full of change

for i in range(50):
    coins.append(random.choice(types_of_coins))
print(coins)
print()

# COUNT HOW MANY COINS OF EACH TYPE (process the data)

for coin in coins:
    if coin not in counted_coins.keys():
        counted_coins[coin] = 1
    else:
        counted_coins[coin] += 1

print(counted_coins)
print()

# (3) CALCULATE THE MONETARY VALUE (calculate and output)
# use code to answer these questions
# Q: What is the monetary value of each type of coin?
# e.g. if I have 3 dimes, I have $0.30 in dimes
# Q: What is the total amount of money in the change cup?

values = {"penny": 0.01, "nickel": 0.05, "dime": 0.1, "quarter": 0.25}
totals = {}

for coin in counted_coins.keys():
    totals[coin] = counted_coins[coin] * values[coin]

total = sum(totals.values())

print(f"Quarters: ${totals['quarter']:.2f}")
print(f"Dimes: ${totals['dime']:.2f}")
print(f"Nickels: ${totals['nickel']:.2f}")
print(f"Pennies: ${totals['penny']:.2f}")
print(f"\nTotal change in cup: ${total:.2f}\n")