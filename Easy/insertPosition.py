# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
# Input: nums = [1,3,5,6], target = 5
# Output: 2

# Example 2:
# Input: nums = [1,3,5,6], target = 2
# Output: 1

def searchInsert(nums, target):
    N = len(nums)
    r= N - 1
    l = 0

    while l<=r:
        mid = l + ((r-l) // 2)
        if(nums[mid] == target):
            return mid
        elif(nums[mid] < target):
            l = mid + 1
        else:
            r = mid - 1

    return l;      

print(searchInsert([1,3,5,6,8], 2))       
print(searchInsert([1,3,5,6,8], 5))    
print(searchInsert([1,3,5,6,8], 15))    
