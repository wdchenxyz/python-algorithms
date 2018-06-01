"""
Use bitwise operator to add/subtract/multiply/divide two numbers

Input:
3 2
Output:
5
"""

def add_bitwise_operator(x, y):
    ''' x + y using bitwise operator
        Idea: Split the non-carry bits and carry bits.
        302 + 099 = 391 + 010 = 301 + 100 = 401 + 000

        x     y     sum   carry
        0     0     0     0
        0     1     1     0
        1     0     1     0
        1     1     0     1

        sum = x ^ y
        carry = x & y
    '''
    
    while y: 
        carry = x & y # use AND to find which bits will result in carry bit
        x = x ^ y # use XOR to add the bits without producing a carry bit
        y = carry << 1 # carry the carry bits one column left
    return x

def subtract_bitwise_operator(x, y):
    ''' x - y using bitwise operator
        Idea: 
        302 - 099 = 313 - 110 = 203 - 000
        split the non-borrow bits and borrow bits

        x    y    diff  borrow    
        0    0    0     0
        0    1    1     1
        1    0    1     0
        1    1    0     0

        diff = x ^ y 
        borrow = (~x) & y
    '''
    while y: 
        borrow = (~x) & y # find which bits will result in borrow bit
        x = x ^ y # use XOR to subtract the bits without producing a borrow bit
        y = borrow << 1 # carry the borrow bits one column left
    return x


    