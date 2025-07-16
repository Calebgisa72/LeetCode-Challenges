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

    zeroT = {}
    initT = {}

    for chr in t:
        zeroT[chr] = 0
        initT[chr] = initT.get(chr,0) + 1

    l = 0
    minWin = ''

    print(zeroT)

    print(initT)

    for r in range(m):
        if s[r] in initT:
            if initT[s[r]] > 0:
               initT[s[r]] -= 1

        while initT == zeroT:
            minWin = s[l:] if r == m-1 else s[l:r+1]
            l += 1
            if s[l] in initT:
                initT[s[l]] = 1
    
    return minWin


print(minWindow('ADOBECODEBANC', "ABC"))
