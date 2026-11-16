labels = ["Name", "Age"]
people = [("Sam", 20), ("Juniper", 18), ("Adam", 22), ("Susan", 19), ("Daniel", 21)]
width = 10

# Add your code here!
print(f"{labels[0] :<{width}}{labels[1] :<{width}}")
print("-" * width * 2)
for (name, age) in people:
    print(f"{name :<{width}}{age :<{width}}")
print()

