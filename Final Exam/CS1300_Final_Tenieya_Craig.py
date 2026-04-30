
# PROBLEM 1 - Compound Interest Calculator

# Figuring out the prompts for users
principal_prompt = (float(input("Principal: ")))
annual_interest_rate = (float(input("Rate (%): ")))
number_of_years = (int(input("Years: ")))

# Loop for computing ending balance year-by-year
for i in range(1, number_of_years + 1):
    balance = principal_prompt * (1 + annual_interest_rate/100) ** i
    print(f"Year {i}: ${balance:.02f}")
    
print(f"Total Interest Earned: ${balance - principal_prompt:.02f}")



# PROBLEM 5 - Simple Expense Tracker

descriptions = []
amounts = []

while True: 
    print("\nExpense Tracker Menu")
    print("1. Add expense")
    print("2. View all expenses")
    print("3. Total Spent")
    print("4. Largest Expense")
    print("5. Remove Expense (by number)")
    print("6. Quit")
    
    choice = input("Choose an option: ")
    if choice == '1':
        desc = input("Enter description: ")
        # Value Error so user can't put in numbers
        try:
            amt = float(input("Enter amount: "))
            if amt < 0:
                print("Must be greater than 0")
            else: 
                descriptions.append(desc)
                amounts.append(amt)
        except ValueError:
            print("Invalid Amount.")

# Views all of the expenses, but makes sure to include zero
    elif choice == "2":
        if len(descriptions) == 0:
            print("No expenses recorded.")
        else:
            for i in range(len(descriptions)):
                print(f"{i+1}. {descriptions[i]}: ${amounts[i]:.2f}")

# Gives entire total
    elif choice == "3":
        total = sum(amounts)
        print(f"Total: ${total:.2f}")

# Compares to see which expense is the most expensive ones
    elif choice == "4":
        if len(amounts) == 0:
            print("No expenses to compare.")
        else:
            largest_index = amounts.index(max(amounts))
            print(f"Largest: {descriptions[largest_index]} (${amounts[largest_index]:.2f})")


# Takes out one of the epenses by number and pops them out to delete them
    elif choice == "5":
        try:
            num = int(input("Enter expense number to remove: "))
            if 1 <= num <= len(descriptions):
                descriptions.pop(num - 1)
                amounts.pop(num - 1)
            else:
                print("Invalid number.")
        except ValueError:
            print("Invalid number.")

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")