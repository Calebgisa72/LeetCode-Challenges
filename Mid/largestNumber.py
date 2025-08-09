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
    stack = []
    largeNum = '0'
    seen = set()

    for num in nums:
        stack.append([num])

    while stack:
        top = stack.pop()

        if len(top) == len(nums):
            s = sum(x for x in top)

            if s > int(largeNum):
                largeNum = str(s)

        for num in nums:
            print(stack)
            newT = top[:]
            newT.append(num)
            if tuple(newT) not in seen and num not in newT:
                stack.append(newT)
                seen.add(tuple(newT))
    
    return largeNum

print(largestNumber([10,2]))