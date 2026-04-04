class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        visited = [[False]*m for i in range(n)]
        def func(i, j): #find the first place where it is 1
            if i>=n or j>=m or j<0 or i<0:
                return 1

            if grid[i][j] == 0:
                return 1
            
            if visited[i][j]:
                return 0
                
            visited[i][j] = True
            
            p1 = func(i+1, j)
            p2 = func(i-1, j)
            p3 = func(i, j+1)
            p4 = func(i, j-1)

            return p1+p2+p3+p4
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return func(i,j) 