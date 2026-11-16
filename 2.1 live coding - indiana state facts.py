'''
indiana_capital = "Indianapolis"
indiana_county_num = 92

capital_input = input("What is the capital of Indiana? ")
if capital_input == indiana_capital:
    answer_capital = True
else: answer_capital = False
print("Your answer is:", answer_capital, "\nThe correct answer is:", indiana_capital)

counties_input = int(input("How many counties are there in Indiana? "))
if counties_input == indiana_county_num:
    answer_counties = True
else: answer_counties = False
print("Your answer is:", answer_counties, "\nThe correct answer is:", indiana_county_num)
'''

indiana_capital = "Indianapolis"
indiana_county_num = 92

capital_input = input("What is the capital of Indiana? ")
print("Your answer is:", capital_input == indiana_capital)
if not(capital_input == indiana_capital):
    print("The correct answer is:", indiana_capital)

counties_input = input("How many counties are there in Indiana? ")
print("Your answer is:", counties_input == str(indiana_county_num))
if not(counties_input == str(indiana_county_num)):
    print("The correct answer is:", str(indiana_county_num))