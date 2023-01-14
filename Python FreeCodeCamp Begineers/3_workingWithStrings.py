"""
Working with Strings.

create a string with "".

lower() to change a character to lowercase or upper() for uppercase.

islower() or isupper() to return a boolean to check case sensitivity.

len(str) to count the number of characters in a string.

Strings = arrays

index(char) to return index of a char
index(str) to return index of a substring

replace(str1, str2) to replace str1 with str2 and return new string

"""

print("A".lower())
print("a".upper())
print("A".isupper())
print("A".islower())
print(len("AAAA"))
a = "Star"
print(a[0])
print(a.index("S"))
print(a.index("St"))
a = a.replace("Star", "Is a Star")
print(a)
