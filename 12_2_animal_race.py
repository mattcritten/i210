import random as r

# functions
def animal_race():
    # initialize values for the remaining distance for each animal
    remainingDistanceTortoise = raceDistance
    remainingDistanceHare = raceDistance
    # Use a loop to run the race until there's a winner
    while True:
        # Each time the loop runs, each animal moves between 1 and its speed
        remainingDistanceTortoise -= r.randrange(1, maxSpeedTortoise)
        remainingDistanceHare -= r.randrange(1, maxSpeedHare)
        # Return the winner and the remaining distance for the loser
        if remainingDistanceTortoise <= 0:
            return "Tortoise", remainingDistanceHare
            break
        if remainingDistanceHare <= 0:
            return "Hare", remainingDistanceTortoise
            break
    
# set up - define any global variables here
raceDistance = 20
maxSpeedTortoise = 5
maxSpeedHare = 10

# main
# call the function, receive the return values, and print them here
def main():
    winner, loserDistance = animal_race()
    print(f"The winnner is {winner}! The loser had {loserDistance} left to go.")

if __name__ == "__main__":
   main()

