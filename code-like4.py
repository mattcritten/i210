meeting = {}

while True:
    name = input("Please enter a person's name to add or remove them from the meeting (or \"\" to exit): \n")

    if name == "":
        break

    elif name in list(meeting.keys()):
        remove = input(f"{name} is currently in the meeting - would you like to remove them (y/n)? ")

        if remove == "y":
            meeting.pop(name)
            print(f"{name} was removed.")
        else:
            print(f"{name} was not removed.")

    else:
        vegitarian = input(f"Is {name} vegitarian (y/n or \"\" to cancel)? ")

        if vegitarian == "y":
            vegitarian = "Vegitarian"
        elif vegitarian == "":
            print(f"{name} was not added.")
            continue
        else:
            vegitarian = "Nonvegitarian"

        meeting[name] = vegitarian

print("Meeting Information Summary\n----------------------------")
print(f"The total amount of Guests is: {len(meeting)}\n")

veg = []
nonveg = []
for name, food in meeting.items():
    if food == "Vegitarian":
        veg.append(name)
    else:
        nonveg.append(name)

print("Vegitarian Guests:")
if veg == []:
    print("\tNone Currently")
else:
    for i in veg:
        print(f"\t{i}")

print("\nNonvegitarian Guests:")
if nonveg == []:
    print("\tNone Currently")
else:
    for i in nonveg:
        print(f"\t{i}")

print()