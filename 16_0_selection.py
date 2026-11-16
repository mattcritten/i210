numbers = [18, 3, 9, 6, 12]

for start_index in range(len(numbers) - 1):
   smallest_index = start_index
   for index in range(start_index + 1, len(numbers)):
       if numbers[smallest_index] > numbers[index]:
           smallest_index = index
   
   temp = numbers[start_index]
   numbers[start_index] = numbers[smallest_index]
   numbers[smallest_index] = temp

print(numbers)
