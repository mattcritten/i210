import random, string

#14.1
def generate_random_boggle(height, width):
    boggle = []
    for _ in range(height):
        row = []
        for _ in range(width):
            row.append(random.choice(ALL_LETTERS))
        boggle.append(row)
    return boggle
            

#14.2 - ignore this for part 1!
def print_boggle(boggle):
    for n in range(len(boggle)):
        for letter in boggle[n]:
            print(letter, end=" ")
        print()
            
# Set up
ALL_LETTERS = string.ascii_uppercase

# main
random_boggle = generate_random_boggle(50,50)
print(random_boggle)
print_boggle(random_boggle)