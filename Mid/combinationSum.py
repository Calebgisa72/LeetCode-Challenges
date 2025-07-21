# 39. Combination Sum
# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.
# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.
# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.


# Example 1:
# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]

def combinationSum(candidates, target):
    res,stack = [],[]
    seen = set()

    for num in candidates:
        stack.append([num])
    
    while stack:
        top: list = stack.pop()

        if tuple(sorted(top)) in seen:
            continue

        if sum(top) == target:
            res.append(top[:])
            seen.add(tuple(sorted(top)))
            continue

        if sum(top) > target:
            continue
        
        for num in candidates:
            newT = top[:]
            newT.append(num)
            stack.append(newT)

    return res

print(combinationSum([2,3,5],8))