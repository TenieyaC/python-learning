
# User Profile Generator

first_name = input("Enter your first name: ").title()
last_name = input("Enter your last name: ").title()
birth_year = int(input("Enter your birth year: "))
hobby = input("Enter your favorite hobby: ")

age = 2026 - birth_year

print("=" * 36)
print("USER PROFILE CARD".center(36))
print("=" * 36)

print(f"Name:     {first_name} {last_name}")
print(f"Age:      {birth_year}")
print(f"Hobby:    {hobby}")
print("-" * 36)
print("Thank you for creating your profile!")
print("=" * 36)



# Text Analyzer

sentence = input("Enter a sentence: ")

# Number of characters (including spaces & excluding spaces)
total_char = len(sentence)
no_spaces = len(sentence.replace(" ", ""))

# Number of words & vowels 
words = len(sentence.split())
vowels = "aeiou"
vowel_count = 0

for letter in sentence:
    vowel_count += (vowels.find(letter) != -1)

# Uppercase and Lowercase of sentence & reversed sentence
uppercase = sentence.upper()
lowercase = sentence.lower()
reversed_sentence = sentence[::-1]

first_letter = sentence[0]
starts_capital = first_letter.isupper()

# Ending with punctuation & last letter
last_letter = sentence[-1]
end_punctuation = last_letter in ".!?"


print("\n=== TEXT ANALYZER ===")
print("Total characters (with spaces):", total_char)
print("Total characters (without spaces):", no_spaces)
print("Number of words:", words)
print("Number of vowels:", vowel_count)
print("Uppercase version:", uppercase)
print("Lowercase version:", lowercase)
print("Reversed:", reversed_sentence)
print("Starts with capital:", starts_capital)
print("Ends with punctuation:", end_punctuation)