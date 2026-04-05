class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        n, m = len(grid), len(grid[0])
        ans = 0

        def dfs(i, j):
            if i<0 or j<0 or i>=n or j>=m or grid[i][j] == '0':
                return

            grid[i][j] = '0'

            for dx, dy in directions:
                dfs(i+dx, j+dy)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    dfs(i,j)
                    ans += 1

        return ans