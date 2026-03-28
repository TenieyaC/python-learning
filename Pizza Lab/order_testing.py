# ============================================
# PIZZA ORDER SYSTEM
# CS 1300 — Lecture 6 Lab
# ============================================

# ----- Menu Data (do not modify) -----
sizes = ["Personal (8\")", "Medium (12\")", "Large (16\")", "Party (20\")"]
size_prices = [6.99, 9.99, 12.99, 16.99]
topping_names = ["Pepperoni", "Mushrooms", "Green Peppers", "Onions", "Sausage", "Bacon", "Extra Cheese", "Pineapple"]
topping_price = 1.50  # each topping, any size

# ----- Order Storage -----
order_descriptions = []  # e.g., "Large Pepperoni, Mushrooms"
order_prices = []        # e.g., 15.99

while True:
    print("="*30)
    print("\tPIZZA SIZES")
    print("="*30)
    
    for i in range(len(sizes)):
        print(f"{i+1}. {sizes[i]}  \t{size_prices[i]:>5}")
    print("="*30)
    
    # Ask for pizza size
    try:
        size_choice = int(input("Pick a size (1-4): "))
        if size_choice < 1 or size_choice > 4:
            print("Choose 1-4.")
            continue
    except ValueError:
        print("Please enter a number!")
        continue
    
    # Show toppings
    print("\nTOPPINGS:")
    for i in range(len(topping_names)):
        print(f"{i+1}. {topping_names[i]}")

    # Select toppings
    selected_toppings = []
    user_input = input("Enter Topping Number. Type done to finish: ")

    while user_input.lower() != "done":
        if user_input.isdigit() and 1 <= int(user_input) <= 8:
            topping = topping_names[int(user_input) - 1]
            if topping not in selected_toppings:
                selected_toppings.append(topping)
            else:
                print("Already added!")
        else:
            print("Not a Topping")
        user_input = input("Enter topping number. Type done to finish: ")


    # Calculate price
    price = size_prices[size_choice - 1] + len(selected_toppings) * topping_price
    
    # Store pizza
    order_descriptions.append(f"{sizes[size_choice - 1]} - {', '.join(selected_toppings)}")
    order_prices.append(price)
    
    print(f"Added pizza: {order_descriptions[-1]} - ${price:.2f}")

    # Ask if they want another pizza
    order_another = input("Order another pizza? (y/n): ")
    if order_another.lower() != "y":
        break

# TESTING SUMMARY
print("\nTESTING ORDER SUMMARY:")
for i in range(len(order_descriptions)):
    print(f"{order_descriptions[i]} - ${order_prices[i]:.2f}")