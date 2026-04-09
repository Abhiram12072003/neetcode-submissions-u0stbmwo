class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        q = deque()
        adj = [[] for i in range(numCourses)]
        indegree = [0]*numCourses

        for x, y in prerequisites:
            adj[x].append(y)
            indegree[y] += 1

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
                
        visit = 0
        ans = []
        while q:
            idx = q.popleft()
            ans.append(idx)
            for chd in adj[idx]:
                indegree[chd] -= 1
                if indegree[chd] == 0:
                    q.append(chd)
            visit += 1

        if visit != numCourses:
            return []
        return ans[::-1]