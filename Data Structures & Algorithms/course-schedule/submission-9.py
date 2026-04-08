class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for i in range(numCourses)]
        indegree = [0] * numCourses

        for x, y in prerequisites:
            indegree[y] += 1
            adj[x].append(y)

        q = deque()

        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
        
        finish = 0

        while q:
            front = q.popleft()
            finish += 1
            for node in adj[front]:
                indegree[node] -= 1
                if indegree[node] == 0:
                    q.append(node)
        

        return finish == numCourses 