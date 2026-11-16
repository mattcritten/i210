from random import randint

def dice_roll(number = 5, sides = 6, amount = 1):
    rolls = []
    for _ in range(0, number):
        roll = 0
        for _ in range(0, amount):
            roll += randint(1, sides)
        rolls.append(roll)
    return rolls

def counts(numbers_list):
    numbers_dict = {}
    for i in numbers_list:
        if i not in numbers_dict.keys():
            numbers_dict[i] = 1
        else:
            numbers_dict[i] += 1
    return numbers_dict
    
def histogram(dict, number = 5, sides = 6, amount = 1):
    print(f"Here are the results of {amount} {sides}-sided dice rolled {number} times!")
    for n in range(1, (sides * amount) + 1):
        bar = ""
        if n in dict.keys():
            for _ in range(0, dict[n]):
                bar += "X"
        print(f"{n}: {bar}")

def main():
    num = int(input("How many total dice rolls? "))
    faces = int(input("How many sides on these dice? "))
    roll = int(input("How many dice should be rolled at once? "))
    
    roll_result = dice_roll(num, faces, roll)
    
    print(f"\nRolling {num} times: {roll} {faces}-sided dice and adding them together.")
    print(roll_result)
    print()
    histogram(counts(roll_result), num, faces, roll)
    

if __name__ == "__main__":
    main()