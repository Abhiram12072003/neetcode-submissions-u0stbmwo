class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = defaultdict(list)
        vis = set()

        for i in range(len(prerequisites)):
            x, y = prerequisites[i]
            d[x].append(y)

        def dfsLoop(idx):
            if idx in vis:
                return True
            
            vis.add(idx)            
            for i in d[idx]:
                if dfsLoop(i):
                    return True
            vis.remove(idx)
            return False

        for i in range(numCourses):
            if i in d:
                x = dfsLoop(i)
                if x:
                    return False

        return True