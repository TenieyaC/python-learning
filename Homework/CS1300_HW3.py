# Problem 1: Boolean Expression Evaluator

a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))
c = int(input("Enter value for c: "))

expr1 = a < b < c
expr2 = not (a > b or b > c)
expr3 = a <= b and b <= c

print("\na < b < c:", expr1)
print("not (a > b or b > c):", expr2)
print("a <= b and b <= c:", expr3)

if expr2 == expr3:
    print("\nDe Morgan's confirmed: Expressions 2 and 3 match!")
else:
    print("\nExpressions 2 and 3 do NOT match.")
    

# Problem 2: Weather Advisory System

temperture = int(input("Enter Current Temperture (F): "))
raining = input("Is it Raining? (yes/no): ").format()

if temperture > 100:
    print("EXTREME HEAT WARNING: Stay indoors!")
elif temperture > 85:
    if raining == 'yes':
        print("Warm rain — watch for flash floods")
    else:
        print("Hot and dry -- stay hydrated.")
elif 60 <= temperture <= 85:
    if raining == 'yes':
        print("Grab an umbrella!")
    else:
        print("Nice weather — enjoy your day! ")
elif 32 <= temperture <= 59:
    print("It's cold — bundle up!")
else:
    print("FREEZE WARNING: Roads may be icy!")
    

#Problem 3: Student Grade Report

name = input("Enter Student Name: ")

exam1 = float(input("Enter Exam 1 score: "))
exam2 = float(input("Enter Exam 2 score: "))
exam3 = float(input("Enter Exam 3 score: "))

average = (exam1 + exam2 + exam3) / 3

if average >= 90:
    grade = "A"
elif average >= 87:
    grade = "A-"
elif average >= 83:
    grade = "B+"
elif average >= 80:
    grade = "B"
elif average >= 77:
    grade = "B-"
elif average >= 73:
    grade = "C+"
elif average >= 70:
    grade = "C"
elif average >= 67:
    grade = "C-"
elif average >= 63:
    grade = "D+"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

if average >= 90:
    status = "Dean's List"
elif average >= 70:
    status = "Good Standing"
elif average >= 60:
    status = "Academic Probation"
else:
    status = "Academic Suspension Warning"
    
print("\n============================")
print("    STUDENT GRADE REPORT")
print("============================")
print("Student:", name)
print("Exam 1: ", exam1)
print("Exam 2: ", exam2)
print("Exam 3: ", exam3)
print("----------------------------")
print("Average: {:.2f}".format(average))
print("Grade:  ", grade)
print("Status: ", status)
print("============================")