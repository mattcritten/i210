import sorts

highestPopulatedCountries = {
    "India": 1480000000,
    "China": 1410000000,
    "United States": 349000000,
    "Indonesia": 288000000,
    "Pakistan": 259000000,
    "Nigeria": 242000000,
    "Brazil": 214000000,
    "Bangladesh": 178000000, 
    "Russia": 143000000,
    "Ethiopia": 139000000
}

listHPC = list(highestPopulatedCountries.items())
print(listHPC)
print()

print(sorts.selection_sort(listHPC, 0))
print("-" * 50, "\n")
print()
print(sorts.insertion_sort(listHPC, 1))
print("-" * 50, "\n")
print()



