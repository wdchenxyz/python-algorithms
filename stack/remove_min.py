"""
Given a stack, a function remove_min accepts a stack as a parameter
and removes the smallest value from the stack.

For example:
bottom [2, 8, 3, -6, 7, 3] top
After remove_min(stack):
bottom [2, 8, 3, 7, 3] top

"""

def remove_min(stack):
    
    stack_storage = []

    if len(stack) == 0:
        return stack
    
    min_element = stack.pop()
    stack.append(min_element)
    for _ in range(len(stack)):
        value = stack.pop()
        if value < min_element:
            min_element = value
        stack_storage.append(value)
    
    # backup 
    for _ in range(len(stack_storage)):
        value = stack_storage.pop()
        if value != min_element:
            stack.append(value)
    return stack


case1 = [2, 8, 3, -6, 7, 3]
print(remove_min(case1))