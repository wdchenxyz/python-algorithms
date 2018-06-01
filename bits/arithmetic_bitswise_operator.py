"""
Use bitwise operator to add/subtract/multiply/divide two numbers

Input:
3 2
Output:
5
"""

def add_bitwise_operator(x, y):
    ''' x + y using bitwise operator
        Idea: 302 + 099 = 391 + 010 = 301 + 100 = 401
        Split the non-carry bits and carry bits.
    '''
    
    while y: 
        carry = x & y # use AND to find which bits will result in carry bit
        x = x ^ y # use XOR to add the bits without producing a carry bit
        y = carry << 1 # carry the carry bits one column left
    return x

def subtract_bitwise_operator(x, y):
    pass
    