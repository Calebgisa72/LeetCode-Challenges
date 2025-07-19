# 76. Minimum Window Substring
# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# Example 1:
# Input: s = "ADOAFBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

def minWindow(s, t):
    if not s or not t:
        return ""
    
    from collections import Counter

    t_count = Counter(t)
    window = {}
    have, need = 0, len(t_count)
    res, res_len = [-1, -1], float("inf")
    l = 0

    for r in range(len(s)):
        c = s[r]
        window[c] = window.get(c, 0) + 1

        if c in t_count and window[c] == t_count[c]:
            have += 1

        while have == need:
            if (r - l + 1) < res_len:
                res = [l, r]
                res_len = r - l + 1

            window[s[l]] -= 1
            if s[l] in t_count and window[s[l]] < t_count[s[l]]:
                have -= 1
            l += 1

    l, r = res
    return s[l:r+1] if res_len != float("inf") else ""

print(minWindow('ADOBECODEBANC', "ABC"))

