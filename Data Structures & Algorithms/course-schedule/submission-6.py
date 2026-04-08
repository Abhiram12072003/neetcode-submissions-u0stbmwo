class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = defaultdict(list)
        vis = [False]*numCourses
        visited = [False]*numCourses

        for i in range(len(prerequisites)):
            x, y = prerequisites[i]
            d[x].append(y)
        def dfsLoop(idx):
            visited[idx] = True
            for i in d[idx]:
                if vis[i]:
                    return True
                vis[i] = True
                if dfsLoop(i):
                    return True
                vis[i] = False
            return False
        # print(d)
        for i in range(numCourses):
            if i in d and not visited[i]:
                vis[i] = True
                x = dfsLoop(i)
                if x:
                    return False
                vis[i] = False
        
        return True