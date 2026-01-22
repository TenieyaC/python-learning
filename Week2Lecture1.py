
# Exerise 1.1

# What will each line print?
message = "Hello, Python!"

print(message) # Hello, Python

print(type(message)) # String

number = 42

print(type(number)) # Interger


# Exercise 1.2

first_name = 'Taylor'

age = 21

class_name = "Computer Science"

class_score = 100


# Exercise 1.3

a = 256
b = 256
print(f"a = {a}, id(a) = {id(a)}")
print(f"b = {b}, id(b) = {id(b)}")
print(f"Same object? {id(a) == id(b)}")
print()

c = 257
d = 257
print(f"c = {c}, id(c) = {id(c)}")
print(f"d = {d}, id(d) = {id(d)}")
print(f"Same object? {id(c) == id(d)}")

# a & b are correct from same id. With c & d, their ids are almost the same except for the four-six digit ending. 257 and above are different endings which means false


# Exercise 1.4

email = "johnsmith@email.com"

birth_year = 2026 - 2004

age_calculator = birth_year >= 18

adult_age = "Welcome" if age_calculator else "Sorry, too young"

print(adult_age)


# Excecise 1.5

# Variables are labels instead of containers because they help point to different objects that are inside of a variable so it's clear to
# see what this variable is without having to guess. Without labels, it will be very hard to tell which peice of code goes with what and will 
# be annoying without knowing where a certain calculate/important variable is.