# Get the first user input.
number_1 = int(input("Enter the first number: "))
# Get the second user input.
number_2 = int(input("Enter the second number: "))
# Get the third user input.
number_3 = int(input("Enter the third number: "))

# Use if statement to compare each number.
if number_1 > number_2 and number_1 > number_3:
# If the first number is greater than to the second and third number, first number is the highest number.
    print(f"{number_1} is the highest number.")
elif number_2 > number_1 and number_2 > number_3:
# If the second number is greater than to the first and third number, second number is the highest number.
    print(f"{number_2} is the highest number.")
elif number_3 > number_1 and number_3 > number_2:
# If the third number is greater than to the first and second number, third number is the highest number.
    print(f"{number_3} is the highest number.")
else:
# If all numbers are equal, print "equal".
    print("All input are equal.")