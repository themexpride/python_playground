"""
4.1 - Caching
Cache nonoverlapping 16 bit subwords
    - compute parity of each subword
    - compute parity of all subresults
    - generate cache before calling parity check
Parity Check
    - shift by 6, then 4, then 2, and final check
    - use bitwise-AND as "masking"
    - need a MASK_SIZE set to 16 and the BIT_MASK set to 0xFFFF to be able to
      shift for the 2nd and 4th subword
Result
    - check the parity of 4 subwords and use bitwise-XOR for all with bitwise-AND
      for the 2nd and 4th subwords
Time Complexity:
    - O(n/L) where n is word size and L is width of words
Space Complexity:
    - O(1)
"""

def computed_parity():
    parity_dict = {}
    for word in range(2 ** 16):
        parity = 0
        for bit in range(16):
            if (word >> bit) & 1 == 1:
                parity = 1 - parity
        parity_dict[word] = parity
    return parity_dict

def parity(x):
    MASK_SIZE = 16
    BIT_MASK = 0xFFFF
    return (PRECOMPUTED_PARITY[x >> (3 * MASK_SIZE)] ^
            PRECOMPUTED_PARITY[(x >> (2 * MASK_SIZE)) & BIT_MASK] ^
            PRECOMPUTED_PARITY[(x >> MASK_SIZE) & BIT_MASK] ^
            PRECOMPUTED_PARITY[x & BIT_MASK])

PRECOMPUTED_PARITY = computed_parity()

print(parity(0b1011))
print(parity(0b11001010))
