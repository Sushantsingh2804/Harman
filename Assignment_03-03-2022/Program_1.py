# WAP to print if a number is a palindrome or not
User_input = int(input("Enter a number: "))
Num = User_input  # To perform operations on the orignal value
Temp = 0  # To hold temporary values
rev = 0  # To hold the reverse value
# Reversing the number
while Num > 0:
    temp = Num % 10
    rev = (rev * 10) + temp
    Num = Num // 10
# checking if its a palindrome
if User_input == rev:
    print("It is a PALINDROME")
else:
    print("It is NOT a palindrome")
