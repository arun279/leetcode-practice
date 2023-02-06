class Solution(object):
    def numIslands(self, grid):
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and visited[i][j] == False:
                    self.dfs(grid, i, j, rows, cols, visited)
                    count += 1
        return count

    def dfs(self, grid, i, j, rows, cols, visited):
        if(i < 0 or i >= rows or j < 0 or j >= cols or visited[i][j] or grid[i][j]=="0"):
            return
        visited[i][j] = True 
        self.dfs(grid, i-1, j, rows, cols, visited)
        self.dfs(grid, i+1, j, rows, cols, visited)
        self.dfs(grid, i, j-1, rows, cols, visited)
        self.dfs(grid, i, j+1, rows, cols, visited)


s = Solution()
grid1 =[["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
]
grid2 =[["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
]
print(s.numIslands(grid1)) # Output: 1
print(s.numIslands(grid2)) # Output: 3
