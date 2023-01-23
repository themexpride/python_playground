"""
Data Structures - Lists - Nested List Comprehensions

Initial Expression
    Can be any arbitrary expression
        another list comprehension

Transpose rows and colums
    iterator is another list comprehension
        [[list comp] list comp]
    can be similar to appending a row for every column
        for loop with each iteration appending a list comprehension
        or
        nested for loops appending separately in each iteration
        
Complex flow statements
    choose built-in functions to complex flow statements
        zip() function
"""

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

matrix2 = [[row[i] for row in matrix] for i in range(4)]
print(matrix2)
print()

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed)
print()

transposed = []
for i in range(4):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print(transposed)
print()

transposed = list(zip(*matrix))
print(transposed)
