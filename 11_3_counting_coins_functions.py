# 11.3 counting coins using functions
import random

# (1) write a function "create_cup" 
# that takes an integer for how many coins are in the cup
# and returns a list of coins (listed by name)
# e.g. ['dime', 'quarter', ...]

def create_cup(intCoins):
    # SET-UP
    types_of_coins = ["Pennies", "Nickels", "Dimes", "Quarters", "Half-Dollars"]

    # CREATE A CUP FULL OF CHANGE
    change = []
    for i in range(intCoins):
        change.append(random.choice(types_of_coins))

    return change


# (2) write a function "count_coins" 
# that takes in a list of coins,
# counts the coins and returns a dictionary
# results stored as {type: amount}, e.g. {'dime': 16, ...}

def count_coins(ListOfCoins):
    # COUNT HOW MANY COINS OF EACH TYPE
    counted_coins = {}
    for coin in ListOfCoins:
        # if that type of coin isn't in the dictionary, add it
        if coin not in counted_coins:
            counted_coins[coin] = 1
        # if that type of coin is in the dictionary, add to the value
        else:
            counted_coins[coin] += 1

    return counted_coins


# (3) write a function "print_change" 
# that takes in a dictionary of coins,
# and prints the summary about them.
# There is no need for a return statement!

def print_change(DicOfCoins):
    # (3) CALCULATE THE MONETARY VALUE (calculate and output)
    # use code to answer these questions
    # Q: What is the monetary value of each type of coin?
    # e.g. if I have 3 dimes, I have $0.30 in dimes
    # Q: What is the total amount of money in the change cup?

    values = {"Pennies": 0.01, "Nickels": 0.05, "Dimes": 0.1, "Quarters": 0.25, "Half-Dollars": 0.5}
    totals = {}
    for coin in DicOfCoins.keys():
        totals[coin] = DicOfCoins[coin] * values[coin]
    total = sum(totals.values())
    
    for coin in totals.keys():
        print(f"{coin}: ${totals[coin]:.2f}")
    print(f"\nTotal change in cup: ${total:.2f}")


coins = int(input("How many coins are in the cup?: "))
print()
print_change(count_coins(create_cup(coins)))