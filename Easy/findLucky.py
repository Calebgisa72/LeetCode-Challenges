# Given an array of integers arr which are order in a non decreasing order, a lucky integer is an integer that has a frequency in the array equal to its value using two pointers.

# Return the largest lucky integer in the array. If there is no lucky integer return -1.

# Example 1:

# Input: arr = [2,2,3,4]
# Output: 2
# Explanation: The only lucky number in the array is 2 because frequency[2] == 2.
# Example 2:

# Input: arr = [1,2,2,3,3,3]
# Output: 3
# Explanation: 1, 2 and 3 are all lucky numbers, return the largest of them.

def findLucky(arr):
    luckyNum = -1
    l = 0
    n = len(arr)

    for r in range(n):
        if arr[r] != arr[l]:
            if r - l == arr[l]:
                luckyNum = max(luckyNum, arr[l])
            l = r
    
    if n - l == arr[l]:
        luckyNum = max(luckyNum, arr[l])

    return luckyNum

print(findLucky([1,2,2,3,3,3]))