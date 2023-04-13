"""
4.1 Brute Force Solution
Iterate test each bit
    - XOR between result and expression => result
        - expression is x AND 1
    - bitwise shift x right by 1 => x
Time Complexity: O(n)
    - n is word size
Space Complexity: O(1)
"""

def parity_check(x):
    result = 0
    while x:
        result ^= x & 1
        x >>= 1
    return result

print(parity_check(1011))
print()
print(parity_check(1))
