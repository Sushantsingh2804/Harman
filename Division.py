a = int(input("Enter the first number- "))
b = int(input("Enter the second number- "))

if b != 0:
    quotient = a // b
    reminder = a % b
    print("quotient =", quotient)
    print("reminder =", reminder)
else:
    print("Division by zero not possible")