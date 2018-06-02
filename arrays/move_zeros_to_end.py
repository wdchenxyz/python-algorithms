"""
Write an algorithm that takes an array and moves all of the zeros to the end,
preserving the order of the other elements.
    move_zeros([False, 1, 0, 1, 2, 0, 1, 3, "a"])
    returns => [False, 1, 1, 2, 1, 3, "a", 0, 0]

The time complexity of the below algorithm is O(n).
"""

def move_zeros(array):
    ans = []
    zeros = 0
    for num in array:
        if num is 0: # not using `not i` to avoid 'False', '[]', etc.
            zeros += 1
        else:
            ans.append(num)
    ans.extend([0] * zeros)
    return ans

array = [False, 1, 0, 1, 2, 0, 1, 3, "a"]
ans = move_zeros(array)
print(ans)
            