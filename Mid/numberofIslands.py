# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# Example 1:
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1

def numIslands(grid):
    m,n = len(grid), len(grid[0])
    islands = 0

    def dfs(i,j):
        stack = [(i,j)]
        
        while stack:
            x,y = stack.pop()
            if x >= 0 and x < m and y >= 0 and y < n and grid[x][y] == '1':
                grid[x][y] = '0'
                stack.append((x+1,y))
                stack.append((x-1,y))
                stack.append((x,y+1))
                stack.append((x,y-1))

    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                islands +=1
                dfs(i,j)
    
    return islands

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(numIslands(grid))