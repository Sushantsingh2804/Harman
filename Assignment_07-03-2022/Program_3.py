# Write a function to check weather a string is palindrome or not

def isPalindrome(Input_String):
    Reverse_String = Input_String[::-1]
    return Input_String == Reverse_String


if isPalindrome(input("Enter your string-")):
    print("The string is a palindrome")
else:
    print("The string is NOT a palindrome")
