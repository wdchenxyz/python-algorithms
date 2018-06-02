"""
Fundamental bit operation:
    get_bit(num, i): get an exact bit at specific index
    set_bit(num, i): set a bit at specific index
    clear_bit(num, i): clear a bit at specific index
    toggle_bit(num, i): toggle a bit at specific index
    update_bit(num, i, bit): update a bit at specific index
"""

def get_bit(num, i):
    return (num & (1 << i)) != 0

def set_bit(num, i):
    return (num | (1 << i))

def clear_bit(num, i):
    mask = ~(1 << i)
    return num & mask

def toggle_bit(num, i):
    return num ^ (1 << i)

def update_bit(num, i, bit):
    mask = ~(1 << i)
    return (num & mask) | (bit << i)


    