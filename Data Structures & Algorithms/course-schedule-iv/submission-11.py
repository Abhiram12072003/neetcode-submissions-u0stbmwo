class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        isPrereq = [set() for _ in range(numCourses)]

        for x, y in prerequisites:
            adj[x].append(y)
            indegree[y] += 1
        
        q = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        d = defaultdict(set)
        
        while q:
            x = q.popleft()

            for chd in adj[x]:
                d[chd].add(x)
                d[chd].update(d[x])
                indegree[chd] -= 1
                if indegree[chd] == 0:
                    q.append(chd)

        return [u in d[v] for u, v in queries]