class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        d = defaultdict(set)
        adj = [[] for i in range(numCourses)]

        for x, y in prerequisites:
            adj[y].append(x)

        visited = [False]*numCourses
        print(adj)
        def dfs(x):
            if x in d and d[x]:
                # print("f")
                return d[x]
            
            for chd in adj[x]:
                # print(chd)
                d[x].add(chd)
                li = dfs(chd)
                # print(li, chd)
                d[x] = d[x] | (li if li else set())
                # print(d[x])
            return d[x]
            
            
        for i in range(numCourses):
            # print("#", i)
            # if not visited[i]:
                # print(i, d, visited)
            dfs(i)
        # print(d)
        
        ans = []

        for x, y in queries:
            if x in d[y]:
                ans.append(True)
            else:
                ans.append(False) 
        return ans