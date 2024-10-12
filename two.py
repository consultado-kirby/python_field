# Get the user input.
number = int(input("Enter a number: "))

# Use if statement to check if the number is zero, even, or odd.
if number == 0:
# If the number is equal to zero, print "zero".
    print("zero") 
elif number % 2 == 0:
# If the number is divided into 2 and it has no remainder, print "even".
    print("even")
elif number % 2 != 0:
# If the number is divided into 2 and it has a remainder, print "odd".
    print("odd")