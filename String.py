Sample_String = "This is a sample String"
print(Sample_String)
# casing of string
print("Capitalize: "+Sample_String.capitalize())
print("Case Swap: " + Sample_String.swapcase())
print("Lower case: "+Sample_String.lower())
print("Upper Case: "+Sample_String.upper())

# boolean function
print("Starts with:", Sample_String.startswith("T"))
print("Ends wih: ", Sample_String.endswith("g"))
print("Is alphanumeric: ", Sample_String.isalnum())
print("Contains alphabet: ", Sample_String.isalpha())
print("Contains decimals: ", Sample_String.isdecimal())
print("Contains digits: ", Sample_String.isdigit())
print("Contains Numeric characters: ", Sample_String.isnumeric())
print("Contains lower case: ", Sample_String.islower())
print("Contains upper case: ", Sample_String.isupper())

#Search and edit string functions
print("Find: ", Sample_String.find('x'))
print("Index: ", Sample_String.index('i'))
print("Right index: ", Sample_String.rindex('i'))
print("Count: ", Sample_String.count('i'))
print("Replace: ", Sample_String.replace('i', 'j'))

# print("Center: "+Sample_String.center(50))
# print("Count: ", Sample_String.count('s'))
# print("Ends with: ", Sample_String.endswith("T"))
# print("Find: ", Sample_String.find("c"))
