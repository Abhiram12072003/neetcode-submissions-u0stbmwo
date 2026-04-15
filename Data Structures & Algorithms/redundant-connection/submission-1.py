class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        cycle = set()
        adj = [[] for i in range(len(edges)+1)]

        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)
        
        cyclestart = -1
        vis = [False]*(len(edges)+1)
        def dfs(node, parent):
            nonlocal cyclestart
            if vis[node] == True:
                cyclestart = node
                return True
            
            vis[node] = True
            for chd in adj[node]:
                if chd != parent:
                    if dfs(chd, node):
                        if cyclestart != -1:
                            cycle.add(node)
                        if cyclestart == node:
                            cyclestart = -1
                        return True
            return False
        
        dfs(1, -1)
        print(cycle)
        for x, y in edges[::-1]:
            if x in cycle and y in cycle:
                return [x, y]

        return [-1, -1]