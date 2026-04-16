# Beginner Exercise
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Entire grid:")
print(grid)
print("Center number:", grid[1][1])


print("Grid by rows:")
for row in grid:
    for num in row:
        print(num, end=" ")
    print()


# Intermediate Exercise

scores = [45, 78, 92, 61, 88, 73, 55, 90, 82]
passing_grades = [score for score in scores if score >= 60]

letter_grades = [
    'A' if grade >= 90 else
    'B' if grade >= 80 else
    'C' if grade >= 70 else
    'D'
    for grade in passing_grades
]

print("Passing grades:", passing_grades)
print("Letter grades:", letter_grades)


# Advanced Exercise

multiplication_table = [[row * col for col in range(1, 5)] for row in range(1, 5)]

print("4x4 Multiplication Table:")
for row in multiplication_table:
    for value in row:
        print(f"{value:3}", end=" ")
    print()

def sum_diagonal(matrix):
    total = 0
    for i in range(len(matrix)):
        total += matrix[i][i]
    return total

diagonal_sum = sum_diagonal(multiplication_table)
print("Diagonal sum:", diagonal_sum)

even_numbers = (num for row in multiplication_table for num in row if num % 2 == 0)

print("First 5 even numbers:")
count = 0
for num in even_numbers:
    print(num)
    count += 1
    if count == 5:
        break