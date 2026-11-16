luddy_departments = {"INFO" : "Informatics",
                    "CSCI" : "Computer Science",
                    "ILS" : "Information and Library Science",
                    "ENGI" : "Inteligent Systems Engineering"}

luddy_students = {"Skye" : "INFO",
                  "Kelsey" : "INFO",
                  "Aang" : "INFO",
                  "Harris" : "INFO",
                  "Cleo" : "CSCI",
                  "Priya" : "CSCI",
                  "Zuko" : "CSCI",
                  "Casey" : "CSCI",
                  "Aoife" : "ILS",
                  "Lena" : "ILS",
                  "Carter" : "ILS",
                  "Eliza" : "ENGI",
                  "Alex" : "ENGI",
                  "Ray" : "ENGI",}

# print(luddy_departments)
# print(luddy_students)

print("The departments in the Luddy School are:\n", luddy_departments)

student_name = input("\nPlease enter a student name to add: ")
student_department = input("What department are they in? (code): ")
luddy_students[student_name] = student_department

print("There are currently", len(luddy_students), "in our system.")

students_alphabet = list(sorted(luddy_students.keys()))
print("The student name that occurs first in the alphabet is", students_alphabet[0] + ".")
print("The student name that occurs last in the alphabet is", students_alphabet[-1] + ".")

current_student = input("Please enter the name of a current student: ")
print(current_student, "is in the", luddy_departments[luddy_students[current_student]], "department.")

