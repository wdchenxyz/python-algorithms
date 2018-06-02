"""
insert bit

insert_one_bit(num, bit, i): insert exact one bit at specific position

input: num = 10101 (21)
insert_one_bit(num, 1, 2): 101101 (45)
insert_one_bit(num, 0, 2): 101001 (41)
insert_one_bit(num, 1, 5): 110101 (53)
insert_one_bit(num, 1, 0): 101011 (43)

insert_mult_bits(num, bits, len, i): insert multiple bits with len at specific position

input: num = 101 (5)
insert_mult_bits(num, 7, 3, 1): 101111 (47)
insert_mult_bits(num, 7, 3, 0): 101111 (47)
insert_mult_bits(num, 7, 3, 3): 111101 (61)
"""

def insert_one_bit(num, bit, i):
    mask = num >> i
    mask = (mask << 1) | bit
    mask = mask << i
    miss_part = ((1 << i) - 1) & num
    return mask | miss_part

def insert_mult_bits(num, bits, len, i):
    mask = num >> i
    mask = (mask << len) | bits
    mask = mask << i
    miss_part = ((1 << i) - 1) & num
    return miss_part | mask


num = 21
print(
    insert_one_bit(num, 1, 2),
    insert_one_bit(num, 0, 2),
    insert_one_bit(num, 1, 5),
    insert_one_bit(num, 1, 0)
)

num = 5
print(insert_mult_bits(num, 7, 3, 1),
    insert_mult_bits(num, 7, 3, 0),
    insert_mult_bits(num, 7, 3, 3))

