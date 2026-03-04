# Problem 1: Temperture Converter

temp = float(input("Enter Temperture: "))
scale = input("Enter Scale: ").strip().lower()

if scale == 'c':
    converted = temp * 9/5 + 32
    print(f"{temp:.1f}°C = {converted:.1f}°F")
elif scale == "f":
    converted = (temp - 32) * 5/9
    print(f"{temp:.1f}°F = {converted:.1f}°C")
else:
    print("Invalid scale.")
    
# Problem 4: Course Eligibility Checker

gpa = float(input("Enter GPA (0.0-4.0): "))
credits = int(input("Enter credit hours completed: "))
prereq = input("Prerequisite completed? (yes/no): ").strip().lower()

if gpa >= 3.5 and credits >= 60 and prereq == "yes":
    status = "Approved: You meet all requirements."
elif gpa >= 3.5 and credits >= 60 and prereq != "yes":
    status = "Conditionally approved: Complete the prerequisite first."
elif gpa >= 3.0 and credits >= 45:
    status = "Waitlisted: You may be admitted if space is available."
elif gpa >= 2.0:
    status = "Not eligible yet: Raise your GPA or earn more credits."
else:
    status = "Denied: GPA is below minimum threshold."

print("\n--- Registration Summary ---")
print(f"GPA: {gpa:.2f}")
print(f"Credits: {credits}")
print(f"Prerequisite: {'Yes' if prereq == 'yes' else 'No'}")
print(f"Status: {status}")
print("----------------------------")