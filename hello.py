# First Python Program for this class

name = input("What is your name? ")

print(f"Hello, {name}. Welcome to Python programming.")
print("Python Version Check: ")

import sys
print(sys.version)

# Lil Practice

list = ['Chocolate', 'Gummy', 'Hard']
print(list)
choice = input(f"What type of Candy, {name}? ")

if choice == 'chocolate' & 'gummy' & 'hard':
    print("START OVER.")
    print(choice)

if choice == 'Chocolate':
    print("Hopefully Not Dark Chocolate.")

elif choice == 'Gummy':
    bow = input("Bears or Worms? ")
    
    if bow == 'Bears':
        print("Nice!")
    else: print("Strange.")

else: print("Breaking Your Teeth With that.")
