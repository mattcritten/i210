# Import the random module with an alias
import random as rnd

# List of possible encounters
encounter_list = ["a wild beast", "a hidden treasure", "an old wizard", "a mysterious stranger"]

# List of possible actions
action_list = ["fight", "flee", "talk", "ignore"]

# Step 1: Random Encounter
# Randomly select an encounter from encounter_list and store it in a variable named encounter
encounter = rnd.choice(encounter_list)
print(f"You encounter {encounter}!")

# Step 2: Random Action
# Shuffle action_list, then store the action at index 0 in a variable named action
rnd.shuffle(action_list)
action = action_list[0]
print(f"You decide to {action}.")

# Step 3: Random Reward
# Randomly choose a number between 1 and 10 and store it in a variable named reward
reward = rnd.randint(1, 10)
print(f"You find {reward} gold coins.")

# Step 4: Random Heal
# Use random.uniform to randomly choose a float between 0 and 1, and if it's below 0.2, set a boolean variable named healed to True
if rnd.uniform(0, 1) < 0.2:
    healed = True
else:
    healed = False
print(f"Have you been healed? {healed}")
