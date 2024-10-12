# Get the first user input (x).
number_1 = int(input("Enter the first number (x): "))
# Get the second user input (y).
number_2 = int(input("Enter the second number (y): "))

# Use if statement to compare all the numbers.
if number_1 > 0 and number_2 > 0:
# If the two numbers are greater than 0, they're in quadrant 1. 
    print("In quadrant 1.")
elif number_1 < 0 and number_2 > 0:
# If the first number is less than 0 and the second number is greater than 0, they're in quadrant 2.
    print("In quadrant 2.")
elif number_1 < 0 and number_2 < 0:
# If the two numbers are less than 0, they're in quadrant 3. 
    print("In quadrant 3.")
elif number_1 > 0 and number_2 < 0:
# If the first number is greater than 0 and the second number is less that 0, they're in quadrant 4.
    print("In quadrant 4.")
else:
    print("Not in quadrant.")