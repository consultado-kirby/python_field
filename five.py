# Get the string input
character = str(input("Enter a character: "))

# If statement to identify if it is vowel or consonant.
if character == "a" or character == "e" or character == "i" or character == "o" or character == "u":
# For lowercase vowels.
    print("The character is vowel.")
elif character == "A" or character == "E" or character == "I" or character == "O" or character == "U":
# For uppercase vowels.
    print("The character is vowel.")
else:
# For consonants
    print("The character is consonant.")