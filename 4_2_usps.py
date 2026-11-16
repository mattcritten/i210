mailType_price = {"postcard": 0.35, "letter": 0.55, "small package": 7.50, "medium package": 16 , 'large package': 40.23}
mailSpeed_price = {'standard': 1, 'priority': 1.75, 'first class': 3}

customerType = input('Welcome to the Post Office! What are you shipping today? (postcard, letter, small package, medium package, large package) ')
customerSpeed = input('How fast would you like that shipped? (standard, priority, first class) ')

customerCost = mailType_price[customerType] * mailSpeed_price[customerSpeed]

print(f'Alrighty! To ship a {customerType} with {customerSpeed} shipping, the total cost will be ${customerCost:.2f} USD')