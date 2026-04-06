
# Makes it a float so they can put decimals 
distance = float(input("Enter Distance: "))
unit = input("Enter unit (km/mi): ").lower()

if unit == 'mi':
# if they put mi, it will convert miles into km
    conversion = distance * 1.60934
    print(f"{distance:.2f} mi = {conversion:.2f} km")
elif unit == 'km':
# same thing like mi to km, but turning km to mi
    conversion = distance * 0.621371
    print(f"{distance:2f} km = {conversion:.2f} mi")
else:
    print("Invalid unit.")
    


# Text Statistic Tool

sentence = input("Enter a sentence: ")

# Counting out the vowels so it's easier to get rid of
vowels = "aeiou"
vowel_count = 0
for letter in sentence:
    vowel_count += (vowels.find(letter) != -1)

# How many total characters and words there were
total_chars = len(sentence)
total_words = len(sentence.split())

# Same thing like the vowels
consonants = "bcdfghjklmnpqrstvwxyz"
consonants_count = 0
for letter in sentence:
    consonants_count += (consonants.find(letter) != -1)

average = len(sentence) / total_words

# Long word - Making a seperate qoutation so it won't make an error
long_word = ""
words = sentence.split()

# Tells that if a word is bigger than long_word, that long word will turn into that word
for word in words:
    if len(word) > len(long_word):
        long_word = word

print(f"Total Characters: {total_chars}")
print(f"Total Words: {total_words}")
print(f"Vowels: {vowel_count}")
print(f"Consonants: {consonants_count}")
print(f"Average Word Length: {average}")
print(f"Longest Word: {long_word}")