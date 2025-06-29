# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:

# Input: nums = [5,7,7,8,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]

def searchRange(nums, target):
    N = len(nums)
    l = 0
    r = N-1
    
    while l<=r:
        m = l + (r-l) // 2
        if(target == nums[m]):
            while nums[l] != target:
                l +=1
            while nums[r] != target:
                r -=1  
            return [l,r]    
        elif nums[m] < target:
            l = m+1
        else:
            r = m-1   

    return [-1,-1]    

print(searchRange([5,7,7,8,8,8,10], 8))       
print(searchRange([5,7,7,8,8,10], 7))     
                