# Beginner Exercise

rgb_color = (255, 128, 0)

print(rgb_color[0])
print(rgb_color[1])
print(rgb_color[2])

pallete = []
pallete.append(rgb_color)

print(pallete)


# Intermediate Execercise

student_one = ("Alice", "C", 18)
student_two = ("James", "B-", 18)
student_three = ("Charles", "A+", 18)

classroom = [student_one, student_two, student_three]


print(f"Second Student Name is {classroom[1][0]}")

name, grade, age = classroom[0]

print(f"{name} is {age} years old and earned a grade of {grade}.")


# Advanced Exercise

student_record = ("Jordan", [55, 87, 21], 0)
student_record[1].append(91)

exam_scores = student_record[1]
average = sum(exam_scores) / len(exam_scores)

updated_student_record = (student_record[0], exam_scores, average)
print("Original tuple:", student_record)
print("Updated tuple:", updated_student_record)