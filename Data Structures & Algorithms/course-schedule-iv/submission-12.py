class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = [[False]*numCourses for _ in range(numCourses)]
        res = []

        for x, y in prerequisites:
            adj[x][y] = True
        
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    adj[i][j] = adj[i][j] or (adj[i][k] and adj[k][j])
        
        for x, y in queries:
            res.append(adj[x][y])
        
        return res