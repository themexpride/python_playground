"""
More Control Flow Tools - if statements

if statement
    included in python

elif statement
    0 or more statements
        chained with if statement

else statement
    end of if statement chain
    optional

switch and case statements
    elif is an alternative
    probably recommended to avoid

comparing same value with multiple constants
checking specific types or attribtes
    use match statement
"""

x = int(input("Please enter an integer: "))

if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')
