class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for i in range(numCourses)]
        
        for x, y in prerequisites:
            adj[x].append(y)

        vis, cycle = set(), set()
        lis = []

        def dfs(x):
            if x in cycle:
                return True
                
            if x in vis:
                return False
            cycle.add(x)

            for chd in adj[x]:
                if dfs(chd):
                    return True

            cycle.remove(x)
            vis.add(x)
            lis.append(x)

            return False

        for i in range(numCourses):
            if dfs(i):
                return []
        return lis