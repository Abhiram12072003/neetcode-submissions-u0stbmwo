class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for i in range(numCourses)]
        indegree = [0]*numCourses

        for x, y in prerequisites:
            adj[y].append(x)
            indegree[x] += 1
        lis = []
        
        def dfs(i):
            lis.append(i)
            indegree[i] -= 1
            for chd in adj[i]:
                indegree[chd] -= 1
                if indegree[chd] == 0:
                    dfs(chd)
            # print(indegree)
        
        for i in range(numCourses):
            if indegree[i] == 0:
                dfs(i)
        # print(lis)

        return lis if len(lis) == numCourses else []