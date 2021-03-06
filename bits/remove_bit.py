"""
remove_bit(num, i): remove a bit at specific position.

input: num = 10101 (21)
remove_bit(num, 2): output = 1001 (9)
remove_bit(num, 4): output = 0101 (5)
remove_bit(num, 0): output = 1010 (10)
"""

def remove_bit(num, i):
    # prune the bits after ith bits
    mask = num >> (i + 1)
    mask = mask << i                 
    miss_part = ((1 << i) - 1) & num # find the missing part in original num
    return mask | miss_part

num = 21
print(
    remove_bit(num, 2),
    remove_bit(num, 4),
    remove_bit(num, 0)
)