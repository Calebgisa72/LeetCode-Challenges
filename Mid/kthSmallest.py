# Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.
# Note that it is the kth smallest element in the sorted order, not the kth distinct element.
# You must find a solution with a memory complexity better than O(n2).

# Example 1:
# Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
# Output: 13
# Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13

def kthSmallest(matrix, k):
    allMatrix = []
    for m in matrix:
        allMatrix += m

    import heapq

    heapq.heapify(allMatrix)

    for _ in range(k-1):
        heapq.heappop(allMatrix)
    
    return heapq.heappop(allMatrix)

print(kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 8))