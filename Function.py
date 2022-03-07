# def isEven(a):
#     if a % 2 == 0:
#         return True
#     else:
#         return False
#
# if isEven(int(input("Enter a number-"))) :
#     print("The Number is Even")
# else:
#     print("The Number is Odd")
# def isDivisibleBy8(a):
#     if a % 8 == 0:
#         return True
#     else:
#         return False
#
#
# if isDivisibleBy8(int(input("Enter a number-"))):
#     print("The Number is divisible by 8")
# else:
#     print("The Number is NOT divisible by 8")

# Sum_Of_number = lambda a,b,c : a+b+c


# def test():
#     pass
#
#
# x = [int(i) for i in input("Enter the numbers separated by a comma-").split(",")]
# print("Sum is -", Sum_Of_number(int(input("Enter 1 number-")), int(input("Enter 2 number-")), int(input("Enter 3 number- "))))
# print("Round Function- ", round(12.2545455, 3))
# print("Max Function- ", max(x))

import Calculator_package as cp
print(cp.addNumbers(14, 18))
print(cp.multiplyNumbers(52, 4))
