while True:
    print("Select an option from menu-")
    print("1. Add 2 numbers ")
    print("2. Subtract 2 numbers")
    print("3. Multiply 2 numbers")
    print("4. Divide 2 numbers")
    print("5. EXIT")
    choice = int(input("Enter your choice-"))
    if choice == 1:
        a = int(input("Enter First number-"))
        b = int(input("Enter Second number-"))
        c = a+b
        print("Result= ",c)
    elif choice == 2:
        a = int(input("Enter First number-"))
        b = int(input("Enter Second number-"))
        c = a - b
        print("Result= ", c)
    elif choice == 3:
        a = int(input("Enter First number-"))
        b = int(input("Enter Second number-"))
        c = a * b
        print("Result= ", c)
    elif choice == 4:
        a = int(input("Enter First number-"))
        b = int(input("Enter Second number-"))
        if b != 0:
            c = a - b
            print("Result= ", c)
        else:
            print("Division by zero not possible")
    elif choice == 5:
        break
    else:
        print("Invalid Choice!!")
