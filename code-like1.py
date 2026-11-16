names = ["Maya", "Leo", "Sofia", "Kai"]

names.append(input("Please enter the name of the additional guest: "))

print('\nHow many guests do we have?', len(names), '\n')

namesSorted = sorted(names)
print("Which guest's name occurs last in the alphabet?", namesSorted[-1], '\n')

print("How many of our guests are named Leo?", names.count("Leo"), '\n')

Event1 = {names[1], names[3], names[4]}
Event2 = {names[1], names[2], names[3]}
Event3 = {names[2], names[3]}

Event3.add(names[-1])
print("Our last guest has requested to also attend Event 3. They are now included!", '\n')

union_event12 = Event1.union(Event2)
union_allevents = union_event12.union(Event3)
print("Are all guests attending at least one event?", union_allevents == names, '\n')

diff_event12 = Event1.intersection(Event2)
diff_allevents = diff_event12.intersection(Event3)
print("Which guests are attending all of the events?", diff_allevents, '\n')
