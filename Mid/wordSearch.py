# 79. Word Search
# Given an m x n grid of characters board and a string word, return true if word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

# Example 1:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true

def exist(board, word):
    from collections import deque
    m,n = len(board), len(board[0])
    t = len(word)

    def dfs(i,j):
        stack = deque()
        stack.append((i,j))
        find = 0
        seen = set()

        while stack:
            if find == t:
                return True
            
            x,y = stack.popleft()

            if x >= 0  and x < m and y >= 0 and y < n and (x,y) not in seen and board[x][y] == word[find]:
                find += 1
                seen.add((x,y))

                stack.append((x,y+1))
                stack.append((x-1,y))
                stack.append((x,y-1))
                stack.append((x+1,y))

    for i in range(m):
        for j in range(n):
            if board[i][j] == word[0] and dfs(i, j):
                return True

    return False

board = [["A","B","C","E"],
         ["S","F","C","S"],
         ["A","D","E","E"]]

print(exist(board, "ABCCED"))