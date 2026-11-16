# 11.2 valid zip
# We will use this function in Part 2 as well!
def valid_zip(code):
    if len(code) == 5:
        return True
    else:
        return False


# Part 2 - READ ME!!!
# write a function called find_zip() that takes a user-entered string as its parameter.
# First, use the valid_zip() function we wrote to check if it is a valid zip code.
# If it is, determine whether it is in Bloomington (you may need to convert it to an integer).
# Return a message about which of these situations you're in.
def find_zip(code):
    if not(valid_zip(code)):
        print("Not a valid zip code.")
    else:
        if 47401 <= int(code) <= 47408:
            print("The zip code is in Bloomington.")
        elif int(code) == 46530:
            print("The zip code is your hometown.")
        else:
            print("The zip code is not in Bloomington.")


# main
# input - get a zip code from the user
zip_code = input("Please enter your zip code: ")

# Part 2
# Call find_zip() on the zip code and receive the result.
# Print a message about the zip code being Bloomington, their home town, or not valid
find_zip(zip_code)