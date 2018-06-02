"""
Use bitwise operator to add/subtract/multiply/divide two numbers
Recommend using C/C++, Python doesn't optimize tail recursion,
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
        x = x ^ y         # use XOR to subtract the bits without producing a borrow bit
        y = borrow << 1   # carry the borrow bits one column left
    return x

def multiply_bitwise_operator(x, y):
    ''' x * y using bitwise operator
        note: using 'add' operator is unavoidable (?)
              could use add_bitwise_operator or arithmetic '+'
        reference: 'russian peasant method'.
                    Let the two given numbers be 'x' and 'y'
                    1) Initialize result 'res' as 0.
                    2) Do following while 'y' is greater than 0
                        a) If 'y' is odd, add 'x' to 'res'
                        b) Double 'x' and halve 'y'
                    3) Return 'res'. 
    '''
    res = 0
    while y:
        # if second number is odd, add the first number to result.
        if (y & 1): 
            res = res + x # '+' could be replace by 'add_bitwise_operator'
        # double the first number and halve the second number
        x = x << 1
        y = y >> 1
    return res

def divide_bitwise_operator(x, y):
    ''' x / y using bitwise operator
        Idea: keep subtracting the divisor from dividend until dividend becomes less than divisor.
            The dividend becomes the remainder, and the number of times subtraction is done becomes the quotient.
    '''

    # sign of the quotient
    # sign = -1 either one of them is negative
    # otherwise sign = 1
    sign = -1 if ((x < 0) ^ (y < 0)) else 1 

    # make both divisor and dividend be positive
    x = abs(x)
    y = abs(y)

    quotient = 0
    while (x >= y):
        x -= y
        quotient += 1
    
    return sign * quotient

"""
Recursion version or other method
"""

def recursion_add(x, y):
    if (y == 0):
        return x
    else:
        return recursion_add(x ^ y, (x & y) << 1)

def recursion_subtract(x, y):
    if (y == 0):
        return x
    else: 
        return recursion_subtract(x ^ y, (~x & y) << 1)

def recursion_multiply(x, y):

    # 0 multiplied with anything gives 0
    if (y == 0):
        return 0
    # add x one by one, y times
    if (y > 0):
        return x + recursion_multiply(x, y - 1)
    # do oppositely
    if (y < 0):
        return -recursion_multiply(x, -y)

def recursion_divide(dividend, divisor):
    
    def quotient(x, y):
        if x < y:
            return 0
        return 1 + quotient(x - y, y)

    sign = -1 if ((dividend < 0) ^ (divisor < 0)) else 1 
    dividend = abs(dividend)
    divisor = abs(divisor)

    return sign * quotient(dividend, divisor)

