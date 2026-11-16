# input - get the population of your hometown.
# store as a number.
hometown_pop = int(input("Enter the population of your hometown: "))

# processing - assign the city name that relates
# to the population given
    # compare to:
    # Ellettsville - 6829
    # Martinsville - 11952
    # Bedford - 13853
    # Bloomington - 79986
    # Fort Wayne - 273203
    # Indianapolis - 900896
populations = {"Ellettsville": 6829, 
               "Martinsville": 11952, 
               "Bedford": 13853, 
               "Bloomington": 79986, 
               "Fort Wayne": 273203, 
               "Indianapolis": 900896,}


# output - compare the hometown to another city.
# outputting a city name that's bigger than the
# hometown population
if hometown_pop > populations["Indianapolis"]:
    print("That's bigger than Indianapolis!")
elif hometown_pop > populations["Fort Wayne"]:
    print("That's bigger than Fort Wayne!")
elif hometown_pop > populations["Bloomington"]:
    print("That's bigger than Bloomington!")
elif hometown_pop > populations["Bedford"]:
    print("That's bigger than Bedford!")
elif hometown_pop > populations["Martinsville"]:
    print("That's bigger than Martinsville!")
elif hometown_pop > populations["Ellettsville"]:
    print("That's bigger than Ellettsville!")
else:
    print("That's smaller than Ellettsville!")
