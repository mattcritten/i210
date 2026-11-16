# Use these values to answer
# the questions using Boolean comparisons

bike_brands = ["Trek", "Specialized", "Giant", "Cannondale", "Santa Cruz", "Scott"]

bike1_brand = "Trek"
bike1_bell = True
bike1_color = "silver"
bike1_kickstand = False
bike1_gears = 21

bike2_brand = "Cannondale"
bike2_bell = True
bike2_color = "purple"
bike2_kickstand = True
bike2_gears = 7

# Are the bicycles the same color and brand?
print("Are the bicycles the same color and brand?")
if bike1_brand == bike2_brand and bike1_color == bike2_color:
    print(f"Yes, both bicycles are {bike1_color} {bike1_brand} bicycles.")
elif bike1_brand == bike2_brand and bike1_color != bike2_color:
    print(f"No, both bicycles are {bike1_brand}, but bike 1 is {bike1_color} and bike 2 is {bike2_color}.")
elif bike1_brand != bike2_brand and bike1_color == bike2_color:
    print(f"No, both bicycles are {bike1_color}, but bike 1 is {bike1_brand} and bike 2 is {bike2_brand}.")
else:
    print(f"No, bike 1 is a {bike1_color} {bike1_brand} bicycle, while bike 2 is a {bike2_color} {bike2_brand} bicycle.")

# Does bike1 have either a bell or a kickstand?
print("Does bike1 have either a bell or a kickstand?")
if bike1_bell == True and bike1_kickstand == True:
    print("Bike 1 has a bell and a kickstand.")
elif bike1_bell == True and bike1_kickstand == False:
    print("Bike 1 has a bell, but not a kickstand.")
elif bike1_bell == False and bike1_kickstand == True:
    print("Bike 1 has a kickstand, but not a bell.")
else:
    print("Bike 1 does not have a bell or kickstand.")

# Do bike2 have more than 3 gears, but less than or 
# equal number of gears than bike1?
print("Do bike2 have more than 3 gears, but less than or equal number of gears than bike1?")
if bike2_gears > 3 and bike2_gears <= bike1_gears:
    print("Yes, Bike 2 has more than 3 gears, and less than or equal to number of gears on bike 1.")
elif bike2_gears > 3 and not bike2_gears <= bike1_gears:
    print("No, Bike 2 has more than 3 gears, but not less than or equal to the number of gears on bike 1.")
elif not bike2_gears > 3 and bike2_gears <= bike1_gears:
    print("No, Bike 2 does not have more than 3 gears, but does have less than or equal to the number of gears on bike 1.")
else:
    print("No, Bike 2 does not have more than 3 gears, and does not have less than or equal to the number of gears on bike 1.")

# Are both bike1 and bike2 in the bike_brands list?
print("Are both bike1 and bike2 in the bike_brands list?")
if bike1_brand in bike_brands and bike2_brand in bike_brands:
    print("Both bikes brands are in the bike_brands list.")
elif bike1_brand in bike_brands and bike2_brand not in bike_brands:
    print(f"Only bike 1's brand, {bike1_brand}, is in the bike_brands list.")
elif bike1_brand not in bike_brands and bike2_brand in bike_brands:
    print(f"Only bike 2's brand, {bike2_brand}, is in the bike_brands list.")
else:
    print("Neither bikes' brand is in the bike_brands list.")