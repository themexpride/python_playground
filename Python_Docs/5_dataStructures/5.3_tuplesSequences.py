"""
Data Structures - Tuples and Sequences

Sequence Type
    Part of list, tuple, range
        Standard sequence data type

Tuple
    Number of values separated by commas
    Don't need to include commas in Python
        Other languages require it

Tuple Features
    Can be Nested
    Immutable
    Can contain mutable objects
    Output enclosed in parentheses
        Regardless of input including/excluding parentheses
    
Parentheses
    Use them when possible
        Needed with larger expressions

Assignment
    Can assign ALL values initially
    Cannot assign values AFTER INITIAL ASSIGNMENT

Accessing
    Unpacking
    Indexing

Tuples with 0 or 1 items
    0 items
        Empty parentheses
    1 item
        Item with trailing comma

Tuple Packing
    Packing item together in a tuple

Sequence Unpacking
    Using sequence to assign multiple variables

"""

t = 12345, 54321, 'hello!'
print(t[0])

print(t)

u = t, (1, 2, 3, 4, 5)
print(u)

# t[0] = 88888 // won't work due to tuple being immutable

v = ([1,2,3], [3,2,1])
print(v)
v[0][1] = 10
print(v)

empty = ()
print(empty, len(empty))

singleton = 'hello',
print(singleton, len(singleton))

t = 12345, 54321, 'hello'
print(t)
x, y, z = t
print(x, y, z)
