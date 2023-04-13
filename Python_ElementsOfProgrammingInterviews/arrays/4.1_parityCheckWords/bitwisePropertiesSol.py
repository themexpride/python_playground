"""
4.1 - Exploiting bitwise operators and bit properties
Parity properties
    - XOR of 0 for 2 bits => 00 or 11
    - XOR computation order doesn't matter
    - we're looking to group bits and then perform XOR to get the parity
    - make sure to know the size of the word we're working with
Example - 11010111
    - Parity of 11010111 = Parity of 1101 XOR Parity of 0111
    - Parity of 1101 = Parity of 11 XOR Parity of 01
    - Parity of 0111 = Parity of 01 XOR Parity of 11
    - Get all these Parities XOR'ed to get the result
    - we're still shifting bits
Time Complexity
    - O(log n) where n is word size
Space Complexity
    - O(1)
"""

def parity(x):
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 0x1

print(parity(11010111))
print(parity(1011))
