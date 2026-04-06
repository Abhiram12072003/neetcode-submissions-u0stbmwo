class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        q = deque()
        n, m = len(grid), len(grid[0])
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((0, i, j))
        cnt = 0
        ps = 0
        while q:
            u, i, j = q.popleft()
            flag = False
            for dx, dy in directions:
                x, y = i+dx, j+dy
                if x<0 or y<0 or x>=n or y>=m:
                    continue
                if grid[x][y] == 1:
                    grid[x][y] += 1
                    flag = True
                    q.append((u+1, x, y))
            if ps != u:
                cnt += 1
            ps = u
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1
        return cnt