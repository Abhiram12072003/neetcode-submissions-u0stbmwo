class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for i in range(n)]
        
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)
        
        vis = set()
        def dfs(x, prev):
            if x in vis:
                return True
            
            vis.add(x)
            for chd in adj[x]:
                if chd == prev:
                    continue
                if dfs(chd,x):
                    return True
            # vis.remove(x)
            return False

        return (not dfs(0, -1)) and len(vis) == n