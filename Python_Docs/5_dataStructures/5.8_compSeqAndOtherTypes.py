"""
Data Structures - Comparing Sequences and Other Types

Sequence Objects - Comparison
    sequence objects use comparison

Comparison - Lexicographical Ordering
    1. first two items compared
    2. next two items compared
    ...
    a recursive process to check if all items are EQUAL COMPARISONS

Some examples
    (1, 2, 3)              < (1, 2, 4)
        3 < 4
    [1, 2, 3]              < [1, 2, 4]
        3 < 4
    'ABC' < 'C' < 'Pascal' < 'Python'
        'A' < 'C'
        'C' < 'P'
        'a' < 'y'
    (1, 2, 3, 4)           < (1, 2, 4)
        3 < 4
    (1, 2)                 < (1, 2, -1)
        null < -1
    (1, 2, 3)             == (1.0, 2.0, 3.0)
        float and int type comparisons are FINE
    (1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)
        'aa' < 'ab' -> 'a' < 'b'

"""
