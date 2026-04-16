# Beginner Exercises

grades = [82, 90, 76]
today_date = (4, 16, 2026)

# Function to boost grades by 5 points
def boost_grades(grade_list):
    for i in range(len(grade_list)):
        grade_list[i] += 5
    return grade_list

updated_grades = boost_grades(grades)
print("Boosted grades:", updated_grades)

# Explanation:
# Lists for grades because lists are mutable (they can change).
# Tuples for the date because dates should not change once set (immutable).


# Intermediate Exercise

def find_range(*args):
    return (min(args), max(args))

print("Range (3 numbers):", find_range(10, 25, 7))
print("Range (7 numbers):", find_range(3, 14, 8, 22, 17, 5, 11))

test_scores = [78, 92, 85, 88, 91]
print("Range (unpacked list):", find_range(*test_scores))


# Advanced Exercises

def calculate_statistics(*args):
    count = len(args)
    total = sum(args)
    average = total / count
    return (count, total, average)

def update_student_records(student_list, bonus):
    updated_list = []

    for name, grade in student_list:
        new_grade = grade + bonus
        updated_list.append((name, new_grade))  # creates a new tuple
    return updated_list

# Example student records
students = [("Chris", 85), ("Brian", 90), ("James", 88)]

# Update grades with bonus
updated_students = update_student_records(students, 5)

print("Updated student records:", updated_students)

grades_only = [grade for name, grade in updated_students]
stats = calculate_statistics(*grades_only)
print("Statistics (count, sum, average):", stats)