# WAP to find square and cube of all given list items using lambda function
x = [int(i) for i in input("Enter the numbers separated by a comma-").split(",")]
Number_Square = list(map(lambda i: i**2, x))
Number_Cube = list(map(lambda i: i**3, x))
print("Square of numbers=", Number_Square)
print("Cube of numbers= ", Number_Cube)
