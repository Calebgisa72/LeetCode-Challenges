# Given a string s, find the length of the longest substring without duplicate characters.
# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

def lengthOfLongestSubstring(s):
    n = len(s)
    seen = set()
    l = 0
    longest = 0

    for r in range(n):
        while s[r] in seen:
            seen.remove(s[l])
            l += 1
        seen.add(s[r])
        w = r - l + 1
        longest = max(longest, w)

    return longest


print(lengthOfLongestSubstring("abcabcghdjakbb"))