"""
Data Structues - Sets

Set
    Unordered collection
    Has no duplicate elements

Uses for set
    Membership Testing
    Eliminating Duplicate Entries

Sets and math operations
    Supports operations
        Union
        Intersection
        Difference
        Symmetric Difference

Creating Set
    Use {}
        Must include vales
    set()

Empty Set
    Created ONLY WITH set()

Set Comprehensions
    Can perform comprehension operations
"""

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

print('orange' in basket)
print('crabgrass' in basket)

a = set('abracadabra')
b = set('alacazam')
print(a)
print(b)
print()
print('a-b')
print(a - b)
print('a | b')
print(a | b)
print('a & b')
print(a & b)
print('a ^ b')
print(a ^ b)
print()
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)
