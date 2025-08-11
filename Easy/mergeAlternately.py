# 1768. Merge Strings Alternately

# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
# Return the merged string.

# Example 1:
# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r

def mergeAlternately(word1, word2):
    from collections import deque
    w1 = deque(word1)
    w2 = deque(word2)
    result = []

    while w1 and w2:
        result.append(w1.popleft())
        result.append(w2.popleft())
    
    if w1:
        result += list(w1)
    if w2:
        result += list(w2)

    return result

print(mergeAlternately([1,3,5],[2,4,6,7,8,9]))