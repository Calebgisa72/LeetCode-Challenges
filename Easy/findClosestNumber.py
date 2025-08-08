# 2239. Find Closest Number to Zero
# Given an integer array nums of size n, return the number with the value closest to 0 in nums. If there are multiple answers, return the number with the largest value.

# Example 2:
# Input: nums = [2,-1,1]
# Output: 1
# Explanation: 1 and -1 are both the closest numbers to 0, so 1 being larger is returned.

def findClosestNumber(nums):
    closest = float('inf')
    for num in nums:
        if abs(num) == abs(closest):
            if num > 0:
                closest = num
        if abs(num) < abs(closest):
            closest = num
    
    return closest

print(findClosestNumber([2,1,1,-1,100000]))