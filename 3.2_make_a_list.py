animals = []
animals.append(input("Animal 1: "))
animals.append(input("Animal 2: "))
animals.append(input("Animal 3: "))

print(animals)

animals.sort
print(animals[0], "is the first in the alphabet.")

print("The list has a length of", len(animals))

animals.remove(animals[-1])
print("We removed", animals[-1], "from the list.")

print(animals)

print("The list has a length of", len(animals))

