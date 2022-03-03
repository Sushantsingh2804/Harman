# WAP to print if a String is a palindrome or not
User_input = input("Enter a phrase : ")
Reverse_string = User_input[::-1]
if User_input == Reverse_string:
    print("It is a PALINDROME")
else:
    print("It is NOT a palindrome")