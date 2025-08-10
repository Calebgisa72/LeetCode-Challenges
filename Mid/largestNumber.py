# 179. Largest Number
# Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.
# Since the result may be very large, so you need to return a string instead of an integer.

# Example 1:
# Input: nums = [10,2]
# Output: "210"

# Example 2:
# Input: nums = [3,30,34,5,9]
# Output: "9534330"

def largestNumber(nums):
    # from collections import Counter
    stack = []
    largeNum = '0'
    seen = set()

    for num in nums:
        stack.append([num])

    while stack:
        numsCopy: list = nums[:]
        top = stack.pop()

        for y in top:
            numsCopy.remove(y)

        if len(top) == len(nums):
            s = ''.join(map(str, top))
            print(f's {s}')

            if int(s) > int(largeNum):
                largeNum = s
            continue

        for num in numsCopy:
            print(stack)
            newT = top[:]
            newT.append(num)
            if tuple(newT) not in seen:
                stack.append(newT)
                seen.add(tuple(newT))
    
    return largeNum

print(largestNumber([3,30,34,5,9]))