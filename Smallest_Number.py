def smallest_number(a, b, c):
    if a < b and a < c:
        return a
    elif b < c:
        return b
    else:
        return c


print("The smallest number is ",
      smallest_number(int(input("Enter 1 number-")), int(input("Enter 2 number-")), int(input("Enter 3 number-"))))
