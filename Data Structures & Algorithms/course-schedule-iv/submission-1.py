class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = [[] for i in range(numCourses)]

        for x, y in prerequisites:
            adj[y].append(x)
        
        d = defaultdict(set)

        def dfs(x):
            if x in d:
                return d[x]
            
            for chd in adj[x]:
                d[x].add(chd)
                d[x] |= dfs(chd)
            
            return d[x]
        
        for i in range(numCourses):
            dfs(i)
        
        vis = []
        for x, y in queries:
            if x in d[y]:
                vis.append(True)
            else:
                vis.append(False)
        return vis