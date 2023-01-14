"""
Using Python as a Calculator - Lists

Lists
    Versatile compound data type
    A list of comma-separated values (items) between square brackets
        [1, 3, 4]
    Can contain items of different types
        [1, "o", 2.0]
        Usually all have the same

Index and Slicing
    Return an item
        list[0]
        list[-1]
    Slice list
        list[-2:]
        Returns new list

Concatenation
    concatenate lists with + operator
        [1,2,3] + [4,5,6]
    concatenate variables and literals
        [1,2,3] + restOfList

Mutable
    Can change content

Add items
    append() method adds items to end of list
        list.append(item)
    Don't attempt to use Slicing to add items unless it's on the back
        Overwriting
    

Replacing items
    Use slicing
        list[2:4] = [10, 11]
    Can remove sublist
        list[2:4] = []

Clearing
    Just assign empty list
        list = []

Length
    Return length of list
        len(list)

Nesting
    Can nest lists
        list[2] = [1,2,3]
    Access nested items
        list[2][0]

"""

l = [1,2,3,4]

print(l[0])
print(l[1])
print(l[-1])
print(l[0:2])
print(l[-2:])

print([1,2,3] + [4,5,6])
print(l + [5,6])

l.append(5)
print(l)

l[2:4] = []
print(l)
l[2:4] = [3,4]
print(l)
l = []
print(l)

l = [1,2,3,4]
print(len(l))

n = [[1,2,3],[4,5,6]]
print(n[0][0])
