class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        d = defaultdict(list)
        for i in range(len(prerequisites)):
            x, y = prerequisites[i]
            d[x].append(y)
        xi = []
        vis = set()
        
        visited = [False] * numCourses

        lis = []
        
        def dfsLoop(idx):
            if idx in vis:
                return True
            
            if d[idx] == []:
                if not visited[idx]:
                    visited[idx] = True
                    lis.append(idx)
                return False
                
            vis.add(idx)

            for i in d[idx]:
                if dfsLoop(i):
                    return True

            if not visited[idx]:
                lis.append(idx)
                visited[idx] = True
            
            vis.remove(idx)
            d[idx] = []

            return False
        lis = []

        for i in range(numCourses):
            if i in d:
                if dfsLoop(i):
                    return []
            else:
                lis.append(i)
            
        return lis
