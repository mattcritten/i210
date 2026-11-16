#15.2
# A teacher has a list of final scores for her class
# Write a program using a list comprehension to figure out what percentage passed her course
# A passing grade for this core course is 70% or more

grades = [90.2, 100, 48.5, 89.8, 73, 78.2, 67, 99, 85.4, 97.1, 93.3, 75.5, 96.9, 100, 55, 88.1, 97.6, 94, 100, 69, 73.3, 78.4, 81.1]

# write a list comprehension that sets scores as either "pass" or "fail"
# e.g. output: ['pass', 'pass', 'fail', ...]
passed = []

# write your loop here!
for grade in grades:
    if grade >= 70:
        passed.append("pass")
    else:
        passed.append("fail")
        
passed_other = ["pass" if grade >= 70 else "fail" for grade in grades]

print(passed)
print(passed_other)
        
# use this information to figure out what percentage of students passed the course
# e.g. output: Percent passed: 82.6%
percentage = passed.count("pass") / len(passed) * 100
print(f"Percent passed: {percentage:.1f}%")

