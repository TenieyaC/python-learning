# Movie Ticket Pricing Program - Problem 1

age = int(input("Enter your age: "))
matinee_input = input("Is this a matinee showing? (yes/no): ").strip().lower()

is_matinee = True if matinee_input == "yes" else False

# Validate age
if age < 0:
    print("Error: Age cannot be negative.")
else:
    # Determine age group and price
    if age < 13:
        age_group = "Child"
        price = 6.00 if is_matinee else 8.00

    elif age <= 17:
        age_group = "Teen"
        price = 7.00 if is_matinee else 10.00

    elif age <= 64:
        age_group = "Adult"
        price = 8.00 if is_matinee else 13.00

    else:
        age_group = "Senior"
        price = 6.00 if is_matinee else 7.00

    print("Age group:", age_group)
    print(f"Ticket price: ${price:.2f}")





# Student Profile Validator - Problem 2

errors = []

student_id = input("Enter student ID: ")
name = input("Enter full name: ")
age_input = input("Enter age: ")
major = input("Enter major: ")

# Student ID validation
if len(student_id) != 8:
    errors.append(f"Student ID must be exactly 8 characters (got {len(student_id)})")

if not student_id[0].isalpha():
    errors.append("Student ID must start with a letter")

if not student_id[1:].isdigit():
    errors.append("Last 7 characters of Student ID must be digits")

# Name validation
if len(name.strip()) < 2:
    errors.append("Name cannot be empty")

# Age validation
try:
    age = int(age_input)
    if age < 16 or age > 99:
        errors.append("Age must be between 16 and 99")
except:
    errors.append("Age must be a valid integer")

# Major validation
valid_majors = ["CS", "IT", "CE", "DS"]
if major.upper() not in valid_majors:
    errors.append(f"Major must be one of: CS, IT, CE, DS (got {major})")

# Output results
if len(errors) == 0:
    print("✓ Profile created successfully!")
    print("Student ID:", student_id)
    print("Name:      ", name)
    print("Age:       ", age)
    print("Major:     ", major.upper())
else:
    print("✗ Profile has errors:")
    for error in errors:
        print("-", error)
        




# Campus Cafe Order System - Problem 3

print("==============================")
print("    CAMPUS CAFÉ ORDER SYSTEM")
print("==============================")
print("1. Coffee       - $3.50")
print("2. Sandwich     - $6.00")
print("3. Salad        - $5.50")
print("4. Combo        - $8.00")
print("5. Exit")
print("==============================")

choice = input("Enter your choice (1-5): ")

price = 0
item_name = ""

if choice == "1":
    size = input("Coffee size (Small/Medium/Large): ").strip().lower()
    
    if size == "medium":
        price = 4.50
        item_name = "Coffee (Medium)"
    elif size == "large":
        price = 5.50
        item_name = "Coffee (Large)"
    else:
        print("Invalid size. Defaulting to Small.")
        price = 3.50
        item_name = "Coffee (Small)"

elif choice == "2":
    price = 6.00
    item_name = "Sandwich"

    cheese = input("Add cheese? (yes/no): ").strip().lower()
    if cheese == "yes":
        price += 0.75
        item_name += " + Cheese"

elif choice == "3":
    price = 5.50
    item_name = "Salad"

    dressing = input("Choose dressing (ranch/italian/vinaigrette/none): ").strip().lower()
    if dressing not in ["ranch", "italian", "vinaigrette", "none"]:
        print("Invalid dressing. Defaulting to none.")

elif choice == "4":
    price = 8.00
    item_name = "Combo (Sandwich + Coffee)"

    size = input("Coffee size (Small/Medium/Large): ").strip().lower()
    if size == "medium":
        price += 1.00
    elif size == "large":
        price += 2.00

    cheese = input("Add cheese to sandwich? (yes/no): ").strip().lower()
    if cheese == "yes":
        price += 0.75
        item_name += " + Cheese"

elif choice == "5":
    print("Goodbye!")
    exit()

else:
    print("Invalid menu choice.")
    exit()

# Customer info
name = input("Enter your name: ").strip()
while name == "":
    name = input("Name cannot be empty. Enter your name: ").strip()

# Quantity validation
try:
    quantity = int(input("How many? "))
    if quantity <= 0:
        print("Quantity must be positive.")
        exit()
except:
    print("Invalid quantity.")
    exit()

subtotal = price * quantity
tax = subtotal * 0.07
total = subtotal + tax

print("\n==============================")
print("        ORDER RECEIPT")
print("==============================")
print("Customer:", name)
print("Item:    ", item_name)
print("Quantity:", quantity)
print(f"Unit Price: ${price:.2f}")
print(f"Subtotal:   ${subtotal:.2f}")
print(f"Tax (7%):   ${tax:.2f}")
print(f"Total:      ${total:.2f}")
print("==============================")
print("Thank you for your order!")