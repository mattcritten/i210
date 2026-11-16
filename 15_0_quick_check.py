numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
letters = ["a", "b", "c", "d", "e", "f", "g"]

mult_by_threes = []
for num in numbers:
    mult_by_threes.append(num * 3 )
print(mult_by_threes)
    
mult_by_threes = []
mult_by_threes = [num * 3 for num in numbers]
print(mult_by_threes)

div_by_threes = []
for num in numbers:
    if num % 3 == 0:
        div_by_threes.append(num)
print(div_by_threes)

div_by_threes = []
div_by_threes = [num for num in numbers if num % 3 == 0]
print(div_by_threes)

big_vowels = []
for letter in letters:
    if letter in "aeiou":
        big_vowels.append(letter.upper())
print(big_vowels)

big_vowels = []
big_vowels = [letter.upper() for letter in letters if letter in "aeiou"]
print(big_vowels)