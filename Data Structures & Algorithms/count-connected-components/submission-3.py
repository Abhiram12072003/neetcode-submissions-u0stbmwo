class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for i in range(n)]

        for x,y in edges:
            adj[x].append(y)
            adj[y].append(x)
       
        cnt = 0
        vis = [False]*n

        def dfs(i):
            vis[i] = True
            for chd in adj[i]:
                if not vis[chd]:
                    dfs(chd)
            return

        for i in range(n):
            if not vis[i]:
                dfs(i)
                cnt += 1
        
        return cnt