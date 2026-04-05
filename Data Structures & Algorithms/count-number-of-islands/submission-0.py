class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        
        visited = [[False]*m for i in range(n)]

        
        def dfs(i, j):
            if i<0 or j<0 or i>=n or j>=m:
                return
            
            if visited[i][j] or grid[i][j] == '0':
                return

            visited[i][j] = True
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i, j-1)
            dfs(i, j+1)
            return

        ans = 0
        for i in range(n):
            for j in range(m):
                if not visited[i][j] and grid[i][j] == '1':
                    dfs(i,j)
                    ans += 1
        return ans