"""
Data Structures - Looping Techniques

Dictionaries - Getting key and value at the SAME TIME
    loop through dictionaries and get both key and values
        use items()
            for i, j in dict.items()

Sequences -  Get BOTH index and value
    loop through sequence and get both position index and corresponding value
        use enumerate()
            for index, val in enumerate(list)

Sequences - Loop through 2+ sequences at the SAME TIME
    loop over two or more sequences
        use zip() function
            for a, b in zip(apples, bananas)

Sequences - Loop in REVERSE
    loop over a sequence in reverse
        specify sequence in forward direction - normal range
            then pass-in reversed() call
                reversed(range())

Sequences - Sorted order loop
    loop over sorted order
        use sorted() to return a new sorted list - OG remains intact
            sorted(list)

Sequences - ELIMINATE DUPLICATES
    loop over sequence with unique elements
        set(list)

Looping and CHANGING DURING ITERATION
    avoid doing that
    make a new sequence instead

"""

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for i, j in knights.items():
    print(i, j)

for ind, val in enumerate(['tic', 'tac', 'toe']):
    print(ind, val)

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print(f'What is your {q}? It is {a}')

for i in reversed(range(1, 10, 2)):
    print(i)

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket):
    print(i)

for i in sorted(set(basket)):
    print(i)

