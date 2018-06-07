"""
Given a stack, switch_pairs function takes a stack as a parameter and that
switches successive pairs of numbers starting at the bottom of the stack.

For example, if the stack initially stores these values:
bottom [3, 8, 17, 9, 1, 10] top
Your function should switch the first pair (3, 8), the second pair (17, 9), ...:
bottom [8, 3, 9, 17, 10, 1] top

if there are an odd number of values in the stack, the value at the top of the
stack is not moved: For example:
bottom [3, 8, 17, 9, 1] top
It would again switch pairs of values, but the value at the top of the stack (1)
would not be moved
bottom [8, 3, 9, 17, 1] top

Note: There are 2 solutions:
first_switch_pairs: it uses a single stack as auxiliary storage
second_switch_pairs: it uses a single queue as auxiliary storage
"""

def switch_pairs(stack):

    stack_storage = []
    for _ in range(len(stack)):
        stack_storage.append(stack.pop())
    
    for _ in range(len(stack_storage)):
        if len(stack_storage) == 0:
            break
        first_element = stack_storage.pop()
        if len(stack_storage) == 0:
            stack.append(first_element)
            break
        second_element = stack_storage.pop()
        stack.append(second_element)
        stack.append(first_element)
    return stack

case1 = [3, 8, 17, 9, 1, 10]
case2 = [3, 8, 17, 9, 1]

print(switch_pairs(case1))
print(switch_pairs(case2))