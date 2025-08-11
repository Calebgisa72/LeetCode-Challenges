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
    nums_str = list(map(str, nums))
    
    # Custom comparator
    def compare(a, b):
        if a + b > b + a:
            return -1
        elif a + b < b + a:
            return 1
        else:
            return 0
    
    # Sort with the custom comparator
    nums_str.sort(key=cmp_to_key(compare))
    
    # Join the result
    result = ''.join(nums_str)

print(largestNumber([0,9,8,7,6,5,4,3,2,1]))