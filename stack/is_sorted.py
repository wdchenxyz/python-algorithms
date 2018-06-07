"""
Given a stack, a function is_sorted accepts a stack as a parameter and returns
true if the elements in the stack occur in ascending increasing order from
bottom, and false otherwise. That is, the smallest element should be at bottom

For example:
bottom [6, 3, 5, 1, 2, 4] top
The function should return false
bottom [1, 2, 3, 4, 5, 6] top
The function should return true
"""

def is_sorted(stack):
    stack_storage = []
    for i in range(len(stack)):

        if len(stack) == 0: # empty stack
            return True

        first_element = stack.pop()
        if len(stack) == 0: # only one element in stack
            stack_storage.append(first_element)
            stack += [stack_storage.pop() for _ in range(len(stack_storage))]
            return True
        
        second_element = stack.pop()
        if second_element > first_element:
            stack_storage.append(first_element)
            stack_storage.append(second_element)
            stack += [stack_storage.pop() for _ in range(len(stack_storage))]
            return False

        stack.append(second_element)
        stack_storage.append(first_element)

case1 = [1, 2, 3, 4, 5, 9]
case2 = [1, 3, 9, 7, 8]
case3 = [1]

print(is_sorted(case1))
print(case1)

print(is_sorted(case2))
print(case2)

print(is_sorted(case3))
print(case3)
        