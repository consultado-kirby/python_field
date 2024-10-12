grade = int(input("Enter your grade: "))
if grade > 96:
    print("1.0")
elif grade <= 96 and grade >= 94:
    print("1.25")
elif grade <= 93 and grade >= 91:
    print("1.5")
elif grade <= 90 and grade >= 88:
    print("1.75")
elif grade <= 87 and grade >= 85:
    print("2.0")
elif grade <= 84 and grade >= 82:
    print("2.25")
elif grade <= 81 and grade >= 79:
    print("2.5")
elif grade <= 78 and grade >= 76:
    print("7.5")
elif grade == 75:
    print("3.0")
elif grade <= 74:
    print("5.0")

#else:
#   print("5.0")