"""
More Control Flow Tools - break, continue statements - else clause for loops

break statement
    breaks out innermost enclosing
        for or while loop

else clause
    executed when loop terminated
        exahustion of iterable
        condition becomes false
    not executed when loop terminated by break statement

try-else and loop-else
    both are similar
        not to if-else
    try statement's else executes when no exception occurs
    loop's else executes when no break occurs

continue statement
    skips to next iteration of loop
    
"""

for i in range(10):
    if i % 2 == 0:
        break
    print(i)

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')

for n in range(2, 10):
    if n % 2 == 0:
        print("Even: ", n)
        continue
    print("Odd: ", n)
