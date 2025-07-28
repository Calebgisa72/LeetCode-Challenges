# 643. Maximum Average Subarray I
# You are given an integer array nums consisting of n elements, and an integer k.
# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

# Example 1:
# Input: nums = [1,12,-5,-6,50,3], k = 
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

def findMaxAverage(nums, k):
    currentSum = sum(nums[:k])
    maxSum = currentSum

    for i in range(k,len(nums)):
        currentSum = currentSum + nums[i] - nums[i-k]
        maxSum = max(maxSum,currentSum)
    
    return maxSum/k

print(findMaxAverage([1,12,-5,-6,50,3], 4))