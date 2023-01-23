"""
Data Structures - Lists - List Comprehensions

List Comprehensions
    concise way to create lists
    brackets contain an expression
        followed by for and if clause

Why use?
    Make new lists where each element is result of some operations
        operations applied to each member of another sequence or iterable
    Create subsequence that satisfies a certain condition

Efficiency and Readability
    for loop
        leaves side effects like waste of space
    using constructors and lambda functions
        delivers lists without side effects
    list comprehension
        no side effects
        more concise and readable

Other uses
    call method on each element
    new lists with tuples
    complex expressions and nested functions

"""

squares = []
for i in range(10):
    squares.append(i**2)

print(squares)

squares = list(map(lambda x:x**2, range(10)))
print(squares)

squares = [x**2 for x in range(10)]
print(squares)

combs = [(x, y) for x in [1,2,3] for y in [3,1,4] if x!=y]
print(combs)

freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
freshfruit = [weapon.strip() for weapon in freshfruit]
print(freshfruit)

from math import pi
print([str(round(pi, i)) for i in range(1, 6)])

