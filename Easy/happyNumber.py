# Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:

# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

# Input: n = 19
# Output: true
# Explanation:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1

def isHappy(n):
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            n = sum(int(x)**2 for x in str(n))
        return True

# seen = set()

# def isHappy(n):
#     if n==1:
#         return True
#     if n in seen:
#         return False
#     seen.add(n)
#     return isHappy(sum(int(x)**2 for x in str(n)))

print(isHappy(78999))   # True

    