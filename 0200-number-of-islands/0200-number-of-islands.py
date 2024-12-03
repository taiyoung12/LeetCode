class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid, i, j, row, column):
            if i < 0 or j < 0 or i >= row or j >= column or grid[i][j] == "0":
                return
            
            grid[i][j] = "0"

            dfs(grid, i-1, j, row, column)
            dfs(grid, i+1, j, row, column)
            dfs(grid, i, j-1, row, column)
            dfs(grid, i, j+1, row, column)

        row = len(grid)
        column = len(grid[0])

        answer = 0

        for r in range(row):
            for c in range(column):
                if grid[r][c] == "1":
                    answer+=1
                    dfs(grid, r, c, row, column)

        return answer 