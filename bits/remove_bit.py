"""
remove_bit(num, i): remove a bit at specific position.

input: num = 10101 (21)
remove_bit(num, 2): output = 1001 (9)
remove_bit(num, 4): output = 0101 (5)
remove_bit(num, 0): output = 1010 (10)
"""

def remove_bit(num, i):
    mask = num >> (i + 1)
    mask = mask << i
    miss_part = ((1 << i) - 1) & num
    return num | miss_part