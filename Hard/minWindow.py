# 76. Minimum Window Substring
# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# Example 1:
# Input: s = "ADOAFBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

def minWindow(s, t):
    m = len(s)
    n = len(t)

    if s == t:
        return t 
    
    if m < n:
        return ''
    
    r=0
    l=0
    minWin = float('inf')
    i=0
    window_range = ()
    tClone = t

    while i < m:
        if s[i] in tClone:
            if r == l and tClone == t:
                l = i
            r = i
            tClone = tClone.replace(s[i], '', 1)
            
        if len(tClone) == 0:
            w= r-l+1
            if (minWin > w):
                window_range = (l,r)
                minWin = w
            i = l
            l += 1
            r = l
            tClone = t
        i += 1
    print(window_range)
    
    return s[window_range[0]:window_range[1]+1]


print(minWindow('ADOBECODEBANC', "ABC"))
