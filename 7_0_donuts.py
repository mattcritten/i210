# we have three people in our house with high metabolisms
# each time we order donuts and the box is passed around...
# everyone takes another donut to eat!

donuts = int(input("How many donuts should we buy? "))
print(f"We have {donuts} donuts.")

while donuts:
   donuts -= 3
   print(f"Now {donuts} donuts are left")
  
print("Time to order more donuts!")