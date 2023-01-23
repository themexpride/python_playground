"""
Data Structures - del statement

del statement
    remove slices from a list
        can clear the entire list
        specify the index only
    delete entire variables
"""

a = [1, 2, 3, 4, 5]
print(a)
del a[0:2]
print(a)

a = 0
print(a)
del a
print(a)
