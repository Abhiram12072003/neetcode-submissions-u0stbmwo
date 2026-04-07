class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        n, m = len(heights), len(heights[0])

        def dfs(i, j, vis, prev):
            if i < 0 or j < 0 or i >= n or j >= m:
                return
            if (i, j) in vis:
                return
            if heights[i][j] < prev:
                return

            vis.add((i, j))
            dfs(i-1, j, vis, heights[i][j])
            dfs(i+1, j, vis, heights[i][j])
            dfs(i, j-1, vis, heights[i][j])
            dfs(i, j+1, vis, heights[i][j])
        
        p = set()
        a = set()
        
        for j in range(m):
            dfs(0, j, p, float('-inf'))
            dfs(n-1, j, a, float('-inf'))
        
        for i in range(n):
            dfs(i, 0, p, float('-inf'))
            dfs(i, m-1, a, float('-inf'))
        
        ans = []
        for i in range(n):
            for j in range(m):
                if (i,j) in p and (i,j) in a:
                    ans.append([i, j])
        
        return ans