"""
4.1 - Erase the lowest set bit
Iterate through word
    - XOR between result and 1 -> result
    - AND between x and x-1 (drops lowest set bit of x) -> x
    - return result
Time Complexity:
    - O(k) where k is the number of bits set to 1
Space Complexity:
    - O(1)
"""

def parity_check(x):
    result = 0
    while x:
        result ^= 1
        x &= x - 1
    return result

print(parity_check(1011))
print(parity_check(10001010))
