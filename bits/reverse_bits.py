"""
reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596
(represented in binary as 00000010100101000001111010011100),
return 964176192
(represented in binary as 00111001011110000010100101000000).
"""

def reverse_bits(num):
    res = 0 # result
    i = 0 # counter
    while i < 32:
        res = (res << 1) + (num & 1)
        num >>= 1
        i += 1
    return res