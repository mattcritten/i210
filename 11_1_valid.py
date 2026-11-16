# 11.1 valid zip

# Part 1
# write a function valid_zip that takes an user-entered string and
# checks to see if it is 5 characters long
# note: len() will work on strings, but not integers
# returns True or False
def valid_zip(given):
    if len(given) == 5:
        return True
    else:
        return False

# main
# input - get a zip code from the user
zip_code = input("Please enter your zip code: ")


# Part 1
# processing - make sure the zip is valid
code_valid = valid_zip(zip_code)

# Part 2
# output whether the zip code is valid
print(code_valid)