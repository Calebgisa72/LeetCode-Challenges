# # 78. Subsets

# Given an integer array nums of unique elements, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.

# Example 1:
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

# Example 2:
# Input: nums = [0]
# Output: [[],[0]]

def subsets(nums):
    n = len(nums)
    res,sol = [],[]
    def backtrack(i):
        if i == n:
            res.append(sol[:])
            return
        
        # Ignore nums[i]
        backtrack(i+1)

        # Pick nums[i]
        sol.append(nums[i])
        backtrack(i+1)
        sol.pop()
    
    backtrack(0)
    return res

print(subsets([1,2,3,2]))

