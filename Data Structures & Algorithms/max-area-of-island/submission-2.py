class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[-1, 0], [1,0], [0, -1], [0,1]]
        n, m = len(grid), len(grid[0])
        
        def dfs(i, j):
            if i<0 or j<0 or i>=n or j>=m or grid[i][j] == 0:
                return 0

            grid[i][j] = 0
            
            ans = 1

            for dx, dy in directions:
                ans += dfs(i+dx, j+dy)
            
            return ans
        
        def bfs(i, j):
            q = deque()
            q.append((i,j))
            grid[i][j] = 0
            ans = 0
            while q:
                idx, jdx = q.popleft()
                ans += 1
                for dx, dy in directions:
                    if idx+dx<0 or idx+dx>=n or jdx+dy<0 or jdx+dy>=m or grid[idx+dx][jdx+dy] == 0:
                        continue
                    grid[idx+dx][jdx+dy] = 0
                    q.append((idx+dx, jdx+dy))
            return ans 
        ans = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    # ans = max(dfs(i, j), ans)
                    ans = max(ans, bfs(i,j))
        return ans