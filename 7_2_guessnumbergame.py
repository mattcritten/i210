print("Guess a Number Game v1\nGuess the secret number!\n")
secretNum = 7
guess = int(input("Guess a number between 1 and 10: "))
tries = 1
while guess != secretNum:
    if 10 >= guess > secretNum:
        print("Too High\n")
    elif 1 <= guess < secretNum:
        print("Too Low\n")
    else:
        print("Number not in given range\n")
    guess = int(input("Please try again: "))
    tries += 1
print(f"You guessed it! It was {secretNum}!\nIt took {tries} tries.\n")