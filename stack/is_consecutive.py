"""
Given a stack, a function is_consecutive takes a stack as a parameter and that
returns whether or not the stack contains a sequence of consecutive integers
starting from the bottom of the stack (returning true if it does, returning
false if it does not).

For example:
bottom [3, 4, 5, 6, 7] top
Then the call of is_consecutive(s) should return true.
bottom [3, 4, 6, 7] top
Then the call of is_consecutive(s) should return false.
bottom [3, 2, 1] top
The function should return false due to reverse order.

Note: There are 2 solutions:
first_is_consecutive: it uses a single stack as auxiliary storage
second_is_consecutive: it uses a single queue as auxiliary storage
"""

def first_is_consecutive(stack):
    stack_storage = [] # used to backup stack
    for i in range(len(stack)):
        first_element = stack.pop()
        if len(stack) == 0:
            stack_storage.append(first_element)
            stack += [stack_storage.pop() for _ in range(len(stack_storage))]
            return True
        second_element = stack.pop()
        if first_element - second_element != 1:
            stack_storage.append(first_element)
            stack_storage.append(second_element)
            stack += [stack_storage.pop() for _ in range(len(stack_storage))]
            return False
        stack.append(second_element)
        stack_storage.append(first_element)


case1 = [3, 4, 5, 6, 7]
case2 = [3, 4, 6, 7]
case3 = [1, 2, 3]

print(first_is_consecutive(case1))
print(first_is_consecutive(case2))
print(first_is_consecutive(case3))