from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        n, m = len(grid), len(grid[0])
        
        visited = [[False]*m for i in range(n)]
        def bfs(i, j):
            q = deque()
            grid[i][j] = '0'
            q.append((i,j))
            while q:
                i,j = q.popleft()
                for dx, dy in directions:
                    if i+dx >= 0 and i+dx<n and j+dy >= 0 and j+dy < m and grid[i+dx][j+dy] == '1':
                        q.append((i+dx, j+dy))
                        grid[i+dx][j+dy] = '0'
            return

        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    bfs(i,j)
                    ans += 1
        return ans