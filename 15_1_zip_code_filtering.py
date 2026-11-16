possibles = ['1234', '1234a', '12345', '34', '567890', '67890']

simple_zipcodes = []

# write your loop here!
for zip in possibles:
    if zip.isdigit() and len(zip) == 5:
        simple_zipcodes.append(zip)
        
print(f"Valid Simple Zipcodes: {simple_zipcodes}")

zipcodes = [zip for zip in possibles if zip.isdigit() and len(zip) == 5]

print(f"Valid Simple Zipcodes: {zipcodes}")
