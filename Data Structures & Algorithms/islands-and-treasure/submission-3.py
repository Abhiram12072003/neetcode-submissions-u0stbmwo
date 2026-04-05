class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n, m = len(grid), len(grid[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        q = deque()

        visited = [[False]*m for i in range(n)]
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    q.append((i, j))
                    visited[i][j] = True
             
        while q:
            i, j = q.popleft()
            val = grid[i][j]
            for dx, dy in directions:
                idx, jdx = i+dx, j+dy
                if idx<0 or jdx<0 or idx>=n or jdx>=m or grid[idx][jdx] == -1 or visited[idx][jdx]:
                    continue
                grid[idx][jdx] = min(val+1, grid[idx][jdx])
                q.append((idx, jdx))
                visited[idx][jdx] = True
        return
