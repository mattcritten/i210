students = ["Alice", "Bob", "Charlie", "Daisy", "Ethan", "Fiona", "George", "Hannah", "Isaac", "Jasmine"]

file = open("lesson18/students.txt", "r")
content = file.readlines()
for i in range(len(content)):
    print(f"{i+1}: {content[i].strip()}")
file.close()
