class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for i in range(numCourses)]
        indegree = [0]*numCourses

        for x, y in prerequisites:
            adj[y].append(x)
            indegree[x] += 1
        
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        finish = 0
        lis = []
        while q:
            tp = q.popleft()
            lis.append(tp)
            finish += 1
            for chd in adj[tp]:
                indegree[chd] -= 1
                if indegree[chd] == 0:
                    q.append(chd)

        if finish != numCourses:
            return []
        
        return lis