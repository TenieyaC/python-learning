# ============================================
# PIZZA ORDER SYSTEM
# CS 1300 — Lecture 6 Lab
# ============================================

# ----- Menu Data (do not modify) -----
sizes = ["Personal (8\")", "Medium (12\")", "Large (16\")", "Party (20\")"]
size_prices = [6.99, 9.99, 12.99, 16.99]
topping_names = ["Pepperoni", "Mushrooms", "Green Peppers", "Onions", "Sausage", "Bacon", "Extra Cheese", "Pineapple"]
topping_price = 1.50 # each topping, any size


# ----- Order Storage -----
order_descriptions = [] # e.g., "Large Pepperoni, Mushrooms"
order_prices = [] # e.g., 15.99
# Your code goes below this line.

while True:
    # --- Display size menu (Ex 1) ---
    print ("="*30)
    print ("\tPIZZA SIZES")
    print ("="*30)

    #Loops through and prints the sizes and their price
    for i in range(len(sizes)):
        print(f"{i+1}. {sizes[i]}  \t{size_prices[i]:>5}")
    #Border
    print ("="*30)

# Invalid Sizes and using Try/Except to allow Intergers to pass and repeat the code.
    
    try:
        size_choice = int(input("Pick a size (1-4): "))
        if size_choice < 1 or size_choice > 4:
            print("Choose 1-4.")
        else:
            break
    except ValueError:
        print("Please enter a number!")

# Selecting the topics wanted for the pizza and making sure it passes through with the loop
# --- Select toppings (Ex 3) ---
# ... your code ...

# --- Calculate and store (Ex 4) ---
# ... your code ...

# --- Order another? (Ex 5) ---
# ... your code ...


# ===== POST-ORDER =====
if not order_descriptions:
    print("\nNo pizzas ordered. See you next time!")
else:

# --- Discount code (Ex 8) ---
# ... your code ...
# --- Receipt (Ex 6, updated with discount) ---
# ... your code ...
# --- Most expensive (Ex 7) ---
# ... your code ...
# --- Size breakdown (Ex 9) ---
# ... your code ...
    print("\n Thank you for your order!")
