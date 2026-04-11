class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for i in range(n)]

        for x,y in edges:
            adj[x].append(y)
            adj[y].append(x)
       
        cnt = 0
        vis = [False]*n

        def bfs(i):
            q = deque()
            vis[i] = True
            q.append(i)
            
            while q:
                p = q.popleft()
                for chd in adj[p]:
                    if not vis[chd]:
                        vis[chd] = True
                        q.append(chd)
            

        for i in range(n):
            if not vis[i]:
                bfs(i)
                cnt += 1
        
        return cnt